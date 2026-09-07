import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def seleniumSetup(download_dir=None):
    """
    Set up and return a Chrome WebDriver instance.

    Args:
        download_dir: Optional path to set as Chrome's default download directory.
                      PDFs will be downloaded automatically (not opened in viewer).
                      The directory will be created if it does not exist.
                      After the browser is running, use set_download_directory()
                      to change the download path dynamically per-run.
    """
    # webdriver_manager automatically downloads and installs the correct chromedriver
    # for the current version of Chrome.
    driver_path = ChromeDriverManager().install()

    # Fix for bug where webdriver-manager returns the license file instead of the binary
    if "THIRD_PARTY_NOTICES" in driver_path:
        directory = os.path.dirname(driver_path)
        binary_name = "chromedriver.exe" if os.name == 'nt' else "chromedriver"
        binary_path = os.path.join(directory, binary_name)
        if os.path.exists(binary_path):
            driver_path = binary_path

    # Ensure binary is executable on Unix-like systems
    if os.name != 'nt' and os.path.exists(driver_path):
        current_mode = os.stat(driver_path).st_mode
        if not (current_mode & 0o111):
            os.chmod(driver_path, current_mode | 0o111)

    options = webdriver.ChromeOptions()

    # Configure automatic file downloads (important for PDFs and reports)
    if download_dir:
        os.makedirs(download_dir, exist_ok=True)

    prefs = {
        # Don't prompt for download location
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        # Force PDFs to download as files rather than open in Chrome's viewer
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True,
    }
    if download_dir:
        prefs["download.default_directory"] = os.path.abspath(download_dir)

    options.add_experimental_option("prefs", prefs)

    service = ChromeService(driver_path)
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def set_download_directory(browser, download_path):
    """
    Dynamically change Chrome's download directory for the current session.
    Use this to redirect downloads to a per-run folder without restarting the browser.

    Args:
        browser: A running Selenium Chrome WebDriver instance.
        download_path: Absolute path to the new download directory.
    """
    os.makedirs(download_path, exist_ok=True)
    browser.execute_cdp_cmd("Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": os.path.abspath(download_path),
    })


# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()