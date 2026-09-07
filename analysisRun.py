"""
analysisRun.py

Automates extraction of run artifacts from Navblue PBS Completed Runs.

DOM facts discovered via inspection:
- Completed tab:  <div class="CompletedRunsTab">
- Month dropdown: <select id="run_manager_tab_periods_NNN">
- All tables use absolutely-positioned <div class="TableRow"> / <div class="TableCell">
  (zero <tr> elements exist)
- Signature table rows: <div class="TableRow" id="cr_table_NNN_row_MMM">
  - cell0 = signature name, cell1 = #runs, cell2 = state
- After clicking a signature, run rows appear with a DIFFERENT table prefix
- After clicking a run row, action buttons appear:
    <input class="Button" value="Reports">
    <input class="Button" value="Stats">
    <input class="Button" value="Schedule">
    <input class="Button" value="Dynamic Stats">

Output folder structure:
  <output_dir>/<YYYY-MM>/<Signature>/<RunName>/
      <NNNN>_combined_report.html
      <NNNN>_dynamic_stats.txt
      <NNNN>_schedule.pdf
"""

import os
import re
import time
import glob
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from seleniumSetup import set_download_directory

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _log(msg, cb):
    print(msg)
    if cb:
        cb(msg)

def _wait(browser, timeout=30):
    return WebDriverWait(browser, timeout)

def _safe_name(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

def _wait_for_new_file(download_dir, existing_files, timeout=60, extension=None):
    """
    Wait for a new file to appear in download_dir that is not in existing_files.
    Optionally filter by extension (e.g. '.pdf').
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        current_files = set(glob.glob(os.path.join(download_dir, "*")))
        new_files = current_files - existing_files
        
        # Filter out temporary/incomplete files
        valid_new = []
        for f in new_files:
            if f.endswith(".crdownload") or f.endswith(".tmp"):
                continue
            if extension and not f.lower().endswith(extension.lower()):
                continue
            if os.path.isfile(f):
                valid_new.append(f)
        
        if valid_new:
            # Return the most recently modified new file
            return max(valid_new, key=os.path.getmtime)
        
        time.sleep(0.5)
    return None

def _get_sig_table_prefix(browser):
    """
    Return the ID prefix of the signature table, e.g. 'cr_table_694'.
    This is determined by reading the first TableRow div on the Completed page
    before any signature is clicked.
    """
    rows = browser.find_elements(By.XPATH, "//div[@class='TableRow']")
    if not rows:
        return None
    first_id = rows[0].get_attribute("id") or ""
    # ID format: cr_table_694_row_717 -> prefix is 'cr_table_694'
    parts = first_id.split("_row_")
    return parts[0] if len(parts) == 2 else None

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

def navigate_to_run_manager(browser, log_callback=None):
    """Click the Run Manager tab in the main PBS navigation."""
    def log(m): _log(m, log_callback)
    wait = _wait(browser, 30)

    selectors = [
        (By.CLASS_NAME,        "RunManagerTab"),
        (By.XPATH,             "//*[contains(text(),'Run Manager')]"),
        (By.LINK_TEXT,         "Run Manager"),
        (By.PARTIAL_LINK_TEXT, "Run Manager"),
    ]
    for by, sel in selectors:
        try:
            elem = wait.until(EC.element_to_be_clickable((by, sel)))
            elem.click()
            log("✓ Navigated to Run Manager")
            time.sleep(3)
            return
        except Exception:
            continue

    raise RuntimeError("Could not find Run Manager link. Ensure you are logged in.")


def select_month_and_completed_tab(browser, month_str, log_callback=None):
    """
    1. Click the Completed tab (<div class="CompletedRunsTab">).
    2. Select month_str in the <select id="run_manager_tab_periods_*"> dropdown.
    """
    def log(m): _log(m, log_callback)
    wait = _wait(browser, 30)

    # --- Completed tab ---
    try:
        elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CompletedRunsTab")))
        elem.click()
        log("✓ Clicked Completed tab")
        time.sleep(3)
    except Exception as e:
        log(f"⚠ Could not click Completed tab: {e}")

    # --- Month dropdown (id="run_manager_tab_periods_NNN") ---
    try:
        month_sel = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[contains(@id,'run_manager_tab_periods')]")
        ))
        s = Select(month_sel)
        opts = [o.text.strip() for o in month_sel.find_elements(By.TAG_NAME, "option")]
        match = next((o for o in opts if o == month_str), None)
        match = match or next((o for o in opts if month_str in o), None)
        if match:
            s.select_by_visible_text(match)
            log(f"✓ Selected month: {match}")
            time.sleep(2)
        else:
            log(f"⚠ Month '{month_str}' not found. Available: {opts[:6]}")
    except Exception as e:
        log(f"⚠ Could not select month: {e}")

# ---------------------------------------------------------------------------
# Signatures table
# ---------------------------------------------------------------------------

def get_all_signatures(browser, log_callback=None):
    """
    Read all signature rows from the Completed Runs table.
    Returns (list_of_sig_dicts, sig_table_prefix).

    sig_dict = {"signature": str, "num_runs": int, "state": str}
    sig_table_prefix = e.g. "cr_table_694"
    """
    def log(m): _log(m, log_callback)
    time.sleep(2)

    sig_table_prefix = _get_sig_table_prefix(browser)
    log(f"  Signature table prefix: {sig_table_prefix!r}")

    signatures = []
    page = 1

    while True:
        log(f"  Reading signatures (page {page})…")
        time.sleep(1)

        # Signature rows = TableRow divs whose id starts with the sig table prefix
        if sig_table_prefix:
            xpath = f"//div[@class='TableRow' and starts-with(@id,'{sig_table_prefix}_row_')]"
        else:
            xpath = "//div[@class='TableRow']"

        rows = browser.find_elements(By.XPATH, xpath)
        page_sigs = []
        for row in rows:
            cell0s = row.find_elements(By.XPATH, ".//div[contains(@id,'_cell0_')]")
            cell1s = row.find_elements(By.XPATH, ".//div[contains(@id,'_cell1_')]")
            cell2s = row.find_elements(By.XPATH, ".//div[contains(@id,'_cell2_')]")

            sig_name = cell0s[0].text.strip() if cell0s else ""
            if not sig_name:
                continue
            try:
                num_runs = int(cell1s[0].text.strip()) if cell1s else 0
            except ValueError:
                num_runs = 0
            state = cell2s[0].text.strip() if cell2s else ""
            page_sigs.append({"signature": sig_name, "num_runs": num_runs, "state": state})

        signatures.extend(page_sigs)
        log(f"    {len(page_sigs)} signatures on page {page}")

        # Check for an enabled Next Page button
        try:
            next_btns = browser.find_elements(By.XPATH,
                "//input[@class='ImageButton' and @title='Next Page' and not(@disabled)]")
            if next_btns:
                next_btns[0].click()
                page += 1
                time.sleep(2)
            else:
                break
        except Exception:
            break

    log(f"✓ Total signatures: {len(signatures)}")
    return signatures, sig_table_prefix

# ---------------------------------------------------------------------------
# Clicking a signature and reading its runs
# ---------------------------------------------------------------------------

def click_signature(browser, sig_name, log_callback=None):
    """Click the TableCell div containing sig_name."""
    def log(m): _log(m, log_callback)
    wait = _wait(browser, 20)
    try:
        cell = wait.until(EC.element_to_be_clickable((By.XPATH,
            f"//div[@class='TableCell' and normalize-space(text())='{sig_name}']"
        )))
        cell.click()
        log(f"✓ Clicked signature: {sig_name}")
        time.sleep(3)
    except Exception as e:
        raise RuntimeError(f"Could not click signature '{sig_name}': {e}")


def get_run_rows(browser, sig_table_prefix, log_callback=None):
    """
    After clicking a signature, return the run rows (TableRow divs NOT in the
    signature table). Handles run list pagination.
    """
    def log(m): _log(m, log_callback)
    all_run_rows = []
    page = 1

    while True:
        time.sleep(1)
        all_rows = browser.find_elements(By.XPATH, "//div[@class='TableRow']")

        # Run rows have a different table prefix than the sig table
        if sig_table_prefix:
            run_rows = [r for r in all_rows
                        if not (r.get_attribute("id") or "").startswith(sig_table_prefix)]
        else:
            run_rows = all_rows

        if not run_rows and page == 1:
            log("  ⚠ No run rows found")
            break

        # Extract name from cell0
        page_rows = []
        for row in run_rows:
            cell0s = row.find_elements(By.XPATH, ".//div[contains(@id,'_cell0_')]")
            name = cell0s[0].text.strip() if cell0s else ""
            if name:
                page_rows.append({"name": name, "element": row})

        all_run_rows.extend(page_rows)
        log(f"  Page {page}: {len(page_rows)} runs")

        # Check for run-list next page (look for enabled ImageButton NOT in sig area)
        try:
            next_btns = browser.find_elements(By.XPATH,
                "//input[@class='ImageButton' and @title='Next Page' and not(@disabled)]")
            if next_btns:
                next_btns[0].click()
                page += 1
                time.sleep(2)
            else:
                break
        except Exception:
            break

    log(f"✓ Total runs: {len(all_run_rows)}")
    return all_run_rows

# ---------------------------------------------------------------------------
# Action buttons
# ---------------------------------------------------------------------------

def _click_button(browser, value, timeout=10):
    """Click <input class="Button" value="{value}">. Returns True on success."""
    try:
        btn = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable(
            (By.XPATH, f"//input[@class='Button' and @value='{value}']")
        ))
        btn.click()
        return True
    except Exception:
        return False


def download_combined_report(browser, run_index, run_name, run_folder, log_callback=None):
    """Click Reports → Combined Report, click Generate, click Save in new window, download .txt, then click Done."""
    def log(m): _log(m, log_callback)
    out_path = os.path.join(run_folder, f"{run_index:04d}_combined_report.txt")

    original_handles = set(browser.window_handles)
    wait = _wait(browser, 15)

    # 1. Click Reports button
    if not _click_button(browser, "Reports"):
        log("    ⚠ Reports button not found")
        return
    time.sleep(1)

    # 2. Click Combined Report from the submenu
    clicked = False
    for sel in [
        (By.XPATH, "//*[contains(text(),'Combined Report')]"),
        (By.XPATH, "//*[contains(text(),'Combined')]"),
        (By.XPATH, "//div[@class='MenuItem' and contains(text(), 'Combined')]"),
        (By.XPATH, "//div[@class='MenuItem'][1]"),
    ]:
        try:
            elem = wait.until(EC.element_to_be_clickable(sel))
            elem.click()
            clicked = True
            break
        except Exception:
            continue

    if not clicked:
        log("    ⚠ Combined Report menu item not found")
        return

    time.sleep(2)

    # 3. Click "Generate" button
    try:
        gen_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id, 'generate_combined_report_button_bottom') or @id='generate_combined_report_button_bottom']")
        ))
        gen_btn.click()
        log("    ✓ Clicked Generate Report")
    except Exception as e:
        log(f"    ⚠ Could not find Generate button: {e}")

    time.sleep(3)

    # 4. Handle new window and click "Save"
    try:
        wait.until(lambda d: len(d.window_handles) > len(original_handles))
        new_handle = next(h for h in browser.window_handles if h not in original_handles)
        browser.switch_to.window(new_handle)
        time.sleep(2)

        # Snapshot files before clicking Save
        existing = set(glob.glob(os.path.join(run_folder, "*")))
        set_download_directory(browser, run_folder)
        
        save_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='Save' or contains(@value, 'Save') or contains(text(), 'Save')]")
        ))
        save_btn.click()
        log("    Waiting for combined report download…")
        
        dl_path = _wait_for_new_file(run_folder, existing, timeout=60, extension=".txt")
        if dl_path:
            os.replace(dl_path, out_path)
            log(f"    ✓ Combined report saved: {os.path.basename(out_path)}")
        else:
            log("    ⚠ Combined report download timed out or wrong file type")

        browser.close()
        browser.switch_to.window(list(original_handles)[0])
    except Exception as e:
        log(f"    ⚠ Error downloading report: {e}")
        if len(browser.window_handles) > len(original_handles):
            browser.close()
            browser.switch_to.window(list(original_handles)[0])

    # 5. Click "Done" button
    try:
        done_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id, 'run_reports_done_button') or @id='run_reports_done_button']")
        ))
        done_btn.click()
        log("    ✓ Clicked Reports Done")
    except Exception as e:
        log(f"    ⚠ Could not find Done button: {e}")

    time.sleep(1)


def download_dynamic_stats(browser, run_index, run_name, run_folder, log_callback=None):
    """Click Dynamic Stats, click Save in new window, download .txt."""
    def log(m): _log(m, log_callback)
    out_path = os.path.join(run_folder, f"{run_index:04d}_dynamic_stats.txt")

    original_handles = set(browser.window_handles)
    wait = _wait(browser, 15)

    if not _click_button(browser, "Dynamic Stats"):
        log("    ⚠ Dynamic Stats button not found")
        return

    # Wait for new window
    try:
        wait.until(lambda d: len(d.window_handles) > len(original_handles))
        new_handle = next(h for h in browser.window_handles if h not in original_handles)
        browser.switch_to.window(new_handle)
        time.sleep(2)

        # Snapshot files before clicking Save
        existing = set(glob.glob(os.path.join(run_folder, "*")))
        set_download_directory(browser, run_folder)
        
        save_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='Save' or contains(@value, 'Save') or contains(text(), 'Save')]")
        ))
        save_btn.click()
        log("    Waiting for dynamic stats download…")

        dl_path = _wait_for_new_file(run_folder, existing, timeout=60, extension=".txt")
        if dl_path:
            os.replace(dl_path, out_path)
            log(f"    ✓ Dynamic stats saved: {os.path.basename(out_path)}")
        else:
            log("    ⚠ Dynamic stats download timed out or wrong file type")

        browser.close()
        browser.switch_to.window(list(original_handles)[0])
    except Exception as e:
        log(f"    ⚠ Dynamic stats error: {e}")
        if len(browser.window_handles) > len(original_handles):
            browser.close()
            browser.switch_to.window(list(original_handles)[0])


def download_schedule(browser, run_index, run_name, run_folder, log_callback=None):
    """Click Schedule, wait for PDF download into run_folder."""
    def log(m): _log(m, log_callback)
    out_path = os.path.join(run_folder, f"{run_index:04d}_schedule.pdf")

    # Clean up any existing 0-byte or crdownload files in the folder first
    for f in glob.glob(os.path.join(run_folder, "*")):
        if f.endswith(".crdownload") or os.path.getsize(f) == 0:
            try: os.remove(f)
            except: pass

    # Snapshot files before clicking Schedule
    existing = set(glob.glob(os.path.join(run_folder, "*")))
    set_download_directory(browser, run_folder)
    time.sleep(0.5)

    if not _click_button(browser, "Schedule"):
        log("    ⚠ Schedule button not found")
        return

    log("    Waiting for PDF…")
    dl_path = _wait_for_new_file(run_folder, existing, timeout=60, extension=".pdf")
    if dl_path:
        # Double check file size for PDF
        if os.path.getsize(dl_path) == 0:
            log("    ⚠ Downloaded PDF is empty, retrying wait…")
            time.sleep(2)
            dl_path = _wait_for_new_file(run_folder, existing, timeout=10, extension=".pdf")

        if dl_path and dl_path != out_path:
            try:
                os.replace(dl_path, out_path)
            except Exception:
                pass
        
        if dl_path:
            log(f"    ✓ Schedule PDF: {os.path.basename(out_path)}")
        else:
            log("    ⚠ PDF download failed (empty file)")
    else:
        log("    ⚠ PDF download timed out or wrong file type")

# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_analysis(browser, month_str, sig_filter, run_scope, single_run_index,
                 output_dir, log_callback=None):
    """
    Main entry point called from app.py.

    Args:
        browser:          Logged-in Chrome WebDriver.
        month_str:        e.g. "June 2026"
        sig_filter:       Substring to match signature names (empty = all).
        run_scope:        "all" or "single"
        single_run_index: 1-based index when run_scope == "single"
        output_dir:       Root output folder
        log_callback:     Optional callable(str) for UI logging
    """
    def log(m): _log(m, log_callback)

    # Build month subfolder e.g. "2026-06"
    try:
        month_dt = datetime.strptime(month_str, "%B %Y")
        month_folder = month_dt.strftime("%Y-%m")
    except ValueError:
        month_folder = _safe_name(month_str)

    base_output = os.path.join(output_dir, month_folder)
    os.makedirs(base_output, exist_ok=True)
    log(f"Output root: {os.path.abspath(base_output)}")

    # Navigate
    navigate_to_run_manager(browser, log_callback)
    select_month_and_completed_tab(browser, month_str, log_callback)

    # Read signatures
    all_sigs, sig_table_prefix = get_all_signatures(browser, log_callback)
    if not all_sigs:
        log("⚠ No signatures found. Check month and page load.")
        return

    # Filter
    if sig_filter.strip():
        filtered = [s for s in all_sigs if sig_filter.lower() in s["signature"].lower()]
        log(f"Filtered to {len(filtered)} signature(s) matching '{sig_filter}'")
    else:
        filtered = all_sigs

    if not filtered:
        log(f"⚠ No signatures match '{sig_filter}'")
        return

    # Process each signature
    for sig_info in filtered:
        sig_name = sig_info["signature"]
        num_runs = sig_info["num_runs"]
        log(f"\n{'='*60}\nSignature: {sig_name}  ({num_runs} runs)\n{'='*60}")

        if num_runs == 0:
            log("  Skipping — 0 runs")
            continue

        sig_folder = os.path.join(base_output, _safe_name(sig_name))
        os.makedirs(sig_folder, exist_ok=True)

        # Click signature to load run list
        try:
            click_signature(browser, sig_name, log_callback)
        except RuntimeError as e:
            log(f"  ⚠ {e}")
            continue

        run_rows = get_run_rows(browser, sig_table_prefix, log_callback)
        if not run_rows:
            log("  ⚠ No run rows found")
            continue

        # Determine which runs to process
        if run_scope == "single":
            idx = single_run_index
            if idx < 1 or idx > len(run_rows):
                log(f"  ⚠ Run index {idx} out of range (1–{len(run_rows)})")
                continue
            to_process = [(idx, run_rows[idx - 1])]
        else:
            to_process = [(i + 1, r) for i, r in enumerate(run_rows)]

        for run_index, run_info in to_process:
            run_name   = run_info["name"]
            # Make folder name unique with index to prevent collisions
            run_folder = os.path.join(sig_folder, f"{run_index:04d}_{_safe_name(run_name)}")
            os.makedirs(run_folder, exist_ok=True)

            log(f"\n  [{run_index:04d}] {run_name}")

            # 1. Combined Report (under Reports button)
            try:
                run_info["element"].click() # Ensure selected
                time.sleep(1)
                download_combined_report(browser, run_index, run_name, run_folder, log_callback)
            except Exception as e:
                log(f"    ⚠ Error in Combined Report: {e}")

            # 2. Dynamic Stats (on main Completed tab)
            try:
                # Re-click to ensure we are out of any sub-panels and the row is active
                browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", run_info["element"])
                run_info["element"].click()
                time.sleep(1)
                download_dynamic_stats(browser, run_index, run_name, run_folder, log_callback)
            except Exception as e:
                log(f"    ⚠ Error in Dynamic Stats: {e}")

            # 3. Schedule PDF
            try:
                run_info["element"].click()
                time.sleep(1)
                download_schedule(browser, run_index, run_name, run_folder, log_callback)
            except Exception as e:
                log(f"    ⚠ Error in Schedule PDF: {e}")

    log("\n✅ Analysis complete.")
    try:
        browser.quit()
    except:
        pass
