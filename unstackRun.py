import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from config import *
from run_logger import log_run_to_file

# time between keypresses (0.25 is a known good number)
timeBetween = .025


def unstackRun(prefix, suffix, maxMinCredit, \
               maxIterations, base, seat, \
               min_floor, min_ceiling, min_threshold_hour, min_threshold_minute, \
               normal_floor, normal_ceiling, normal_threshold_hour, normal_threshold_minute, \
               max_floor, max_ceiling, max_threshold_hour, max_threshold_minute, \
               split_low, split_high, split_threshold, \
               maxMixedLines, unstackLineHolders, maxPasses, pointOrDayStack, \
               mixed_low, mixed_high, mixed_threshold, day_settings, \
               browser, testMode, verbose, runNumber, log_callback=None):

    def log(msg):
        if verbose:
            print(msg)
        if log_callback:
            log_callback(msg)

    if seat == "FA":
        runName = prefix + str(runNumber) + "-" + base + "-ALL-FA-" + suffix
        group = base + "-ALL-FA"
    else:
        runName = prefix + str(runNumber) + "-" + base + "-" + seat + "-" + suffix
        group = base + "-XMJ-" + seat

    element = WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@value='Launch Run']"))
    )
    log("Launch page is ready")
    launchButton = browser.find_element("xpath", "//*[@value='Launch Run']")
    launchButton.click()

    groupDropdown = Select(browser.find_element("xpath",
                                                "//*[contains(@id,'add_run_to_queue_rungroups')]"))
    log("selecting " + group)
    groupDropdown.select_by_visible_text(group)

    # set the run name
    runNameTextBox = browser.find_element("xpath",
                                          "//*[contains(@id,'add_run_to_queue_name')]")
    runNameTextBox.send_keys(runName)

    a = []
    a = browser.find_elements(By.CLASS_NAME, "ValidatingText")
    # inputElement = driver.find_element(by=By.NAME, value='quantity')
    # a = browser.find_element("NAME", 'ValidatingText')
    ### below is original line of code that has been decremented
    # a = browser.find_elements_by_class_name("ValidatingText")
    # a = browser.find_element("name", "ValidatingText")
    # a = browser.find_element_by_name("ValidatingText")
    # if verbose:
    # prints a log of all the ValidatingText elements
    #   print(len(a))
    # for element in a:
    #     print("element = ", element.get_attribute("id"), " with value ", element.get_attribute("value"))

    #####################################
    ## Max Iterations
    #####################################
    log("max iterations: " + str(maxIterations))
    time.sleep(timeBetween)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(Keys.BACKSPACE)
    a[0].send_keys(maxIterations)
    a[0].send_keys(Keys.TAB)

    a[3].send_keys(Keys.BACKSPACE)
    a[3].send_keys(Keys.BACKSPACE)
    a[3].send_keys(Keys.BACKSPACE)
    a[3].send_keys(Keys.BACKSPACE)
    a[3].send_keys(maxMixedLines)
    a[3].send_keys(Keys.TAB)

    a[5].send_keys(
        Keys.TAB)  # basically go to the minute portion of the min open credit field (the hour portion is a[3] and the minute portion is a[4]). Then tab to highlight what ends up being a[5}.

    log("normal credit window: " + "floor-" + str(normal_floor) + ", ceiling-" + str(
        normal_ceiling) + ", threshold-" + str(normal_threshold_hour) + ":" + str(normal_threshold_minute))
    log(
        "min credit window: " + "floor-" + str(min_floor) + ", ceiling-" + str(min_ceiling) + ", threshold-" + str(
            min_threshold_hour) + ":" + str(min_threshold_minute))
    log(
        "max credit window: " + "floor-" + str(max_floor) + ", ceiling-" + str(max_ceiling) + ", threshold-" + str(
            max_threshold_hour) + ":" + str(max_threshold_minute))
    log(
        "split credit window: " + "floor-" + str(split_low) + ", ceiling-" + str(split_high) + ", threshold-" + str(
            split_threshold))

    #####################################
    ## Normal credit window
    #####################################
    a[6].send_keys(normal_floor)
    a[6].send_keys(Keys.TAB)
    a[7].send_keys(Keys.TAB)
    a[8].send_keys(normal_ceiling)
    a[8].send_keys(Keys.TAB)
    a[9].send_keys(Keys.TAB)
    a[10].send_keys(normal_threshold_hour)
    a[10].send_keys(Keys.TAB)
    a[11].send_keys(normal_threshold_minute)
    a[11].send_keys(Keys.TAB)

    #####################################
    ## Min credit window
    #####################################
    a[12].send_keys(min_floor)
    a[12].send_keys(Keys.TAB)
    a[13].send_keys(Keys.TAB)
    a[14].send_keys(min_ceiling)
    a[14].send_keys(Keys.TAB)
    a[15].send_keys(Keys.TAB)
    a[16].send_keys(min_threshold_hour)
    a[16].send_keys(Keys.TAB)
    a[17].send_keys(min_threshold_minute)
    a[17].send_keys(Keys.TAB)

    #####################################
    ## Max credit window
    #####################################
    a[18].send_keys(max_floor)
    a[18].send_keys(Keys.TAB)
    a[19].send_keys(Keys.TAB)
    a[20].send_keys(max_ceiling)
    a[20].send_keys(Keys.TAB)
    a[21].send_keys(Keys.TAB)
    a[22].send_keys(max_threshold_hour)
    a[22].send_keys(Keys.TAB)
    a[23].send_keys(max_threshold_minute)
    a[23].send_keys(Keys.TAB)
    if (maxMinCredit != 0):
        a[24].send_keys(Keys.TAB)
        a[24].clear()
        a[24].send_keys(maxMinCredit)
    else:
        a[24].send_keys(Keys.TAB)

    # Add split duty hours
    # If Split Duty Hours = 0, then just use the normal credit windows
    if split_low != 0:
        a[25].send_keys(Keys.TAB)
        a[26].send_keys(Keys.BACKSPACE)
        a[26].send_keys(Keys.BACKSPACE)
        a[26].send_keys(split_low)
        a[27].send_keys(Keys.TAB)
        a[28].send_keys(Keys.BACKSPACE)
        a[28].send_keys(Keys.BACKSPACE)
        a[28].send_keys(split_high)
        a[29].send_keys(Keys.TAB)
        a[30].send_keys(Keys.BACKSPACE)
        a[30].send_keys(Keys.BACKSPACE)
        a[30].send_keys(split_threshold)
        a[30].send_keys(Keys.TAB)
    else:
        a[25].send_keys(Keys.TAB)
        a[26].send_keys(Keys.BACKSPACE)
        a[26].send_keys(Keys.BACKSPACE)
        a[26].send_keys(normal_floor)
        a[27].send_keys(Keys.TAB)
        a[28].send_keys(Keys.BACKSPACE)
        a[28].send_keys(Keys.BACKSPACE)
        a[28].send_keys(normal_ceiling)
        a[29].send_keys(Keys.TAB)
        a[30].send_keys(Keys.BACKSPACE)
        a[30].send_keys(Keys.BACKSPACE)
        a[30].send_keys(normal_threshold_hour)
        a[30].send_keys(Keys.TAB)
        a[31].send_keys(normal_threshold_minute)
        a[31].send_keys(Keys.TAB)

    ####################################
    ## Mixed Lines 
    #####################################
    a[50].send_keys(Keys.BACKSPACE)
    a[50].send_keys(Keys.BACKSPACE)
    a[50].send_keys(mixed_low)
    a[51].send_keys(Keys.TAB)
    a[52].send_keys(Keys.BACKSPACE)
    a[52].send_keys(Keys.BACKSPACE)
    a[52].send_keys(mixed_high)
    a[53].send_keys(Keys.TAB)
    a[54].send_keys(Keys.BACKSPACE)
    a[54].send_keys(Keys.BACKSPACE)
    a[54].send_keys(mixed_threshold)
    a[55].send_keys(Keys.TAB)

    a[56].send_keys(Keys.BACKSPACE)
    a[56].send_keys(Keys.BACKSPACE)
    a[56].send_keys(mixed_low)
    a[57].send_keys(Keys.TAB)
    a[58].send_keys(Keys.BACKSPACE)
    a[58].send_keys(Keys.BACKSPACE)
    a[58].send_keys(mixed_high)
    a[59].send_keys(Keys.TAB)
    a[60].send_keys(Keys.BACKSPACE)
    a[60].send_keys(Keys.BACKSPACE)
    a[60].send_keys(mixed_threshold)
    a[61].send_keys(Keys.TAB)

    a[62].send_keys(Keys.BACKSPACE)
    a[62].send_keys(Keys.BACKSPACE)
    a[62].send_keys(mixed_low)
    a[63].send_keys(Keys.TAB)
    a[64].send_keys(Keys.BACKSPACE)
    a[64].send_keys(Keys.BACKSPACE)
    a[64].send_keys(mixed_high)
    a[65].send_keys(Keys.TAB)
    a[66].send_keys(Keys.BACKSPACE)
    a[66].send_keys(Keys.BACKSPACE)
    a[66].send_keys(mixed_threshold)
    a[67].send_keys(Keys.TAB)

    time.sleep(timeBetween)

    #####################################
    ## Unstack on line holders
    #####################################
    if unstackLineHolders > 0:
        listOfCheckBoxes = []
        listOfCheckBoxes = browser.find_elements(By.CLASS_NAME, "CheckBox")

        # the unstack on lineholder checkbox is the fourth checkbox in the array
        listOfCheckBoxes[4].click()
        time.sleep(timeBetween)

        if verbose:
            # prints a log of all the checkboxes
            print("\nCheckboxes")
            print(len(listOfCheckBoxes))
            for element in listOfCheckBoxes:
                print("checkbox = ", element.get_attribute("id"), " with value ",
                      element.get_attribute("value"))

        # set number of max passes
        try:
            a[49].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
            time.sleep(timeBetween)
            a[49].send_keys(maxPasses)
            time.sleep(timeBetween)
        except:
            print('Issue with the max passes text box')

        listOfRadioButtons = []
        listOfRadioButtons = browser.find_elements(By.CLASS_NAME, "RadioButton")
        if pointOrDayStack == "day":
            listOfRadioButtons[1].click()

        if verbose:
            print("\nRadio Buttons")
            # prints a log of all the radio buttons
            print(len(listOfRadioButtons))
            for element in listOfRadioButtons:
                print("radiobutton = ", element.get_attribute("id"), " with value ",
                      element.get_attribute("value"))

        # set the max stack height for each day
        # Day 1 starts at index 91
        start_index = 91
        for day in range(1, 32):
            index = start_index + (day - 1)
            
            # Check if the index is valid for the current page
            if index >= len(a):
                log(f"Stopping day loop at day {day} (index {index}) - element not found.")
                break
                
            value = day_settings.get(day, 0) # Default to 0 if not provided
            
            try:
                a[index].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
                time.sleep(timeBetween)
                a[index].send_keys(str(value))
                time.sleep(timeBetween)
            except Exception as e:
                log(f"Could not set value for day {day}: Not in this month")


    ####################################
    ## Cancel or save
    #####################################
    settings_dict = {
        "Base": base,
        "Seat": seat,
        "Max Iterations": maxIterations,
        "Max Min Credit": maxMinCredit,
        "Max Mixed Lines": maxMixedLines,
        "Normal Credit Window": f"Floor={normal_floor}, Ceiling={normal_ceiling}, Threshold={normal_threshold_hour:02d}:{normal_threshold_minute:02d}",
        "Min Credit Window": f"Floor={min_floor}, Ceiling={min_ceiling}, Threshold={min_threshold_hour:02d}:{min_threshold_minute:02d}",
        "Max Credit Window": f"Floor={max_floor}, Ceiling={max_ceiling}, Threshold={max_threshold_hour:02d}:{max_threshold_minute:02d}",
        "Split Credit Window": f"Floor={split_low}, Ceiling={split_high}, Threshold={split_threshold}",
        "Mixed Lines Window": f"Low={mixed_low}, High={mixed_high}, Threshold={mixed_threshold}",
        "Unstack Line Holders": unstackLineHolders,
        "Max Passes": maxPasses,
        "Stack Type": pointOrDayStack,
        "Day Settings": day_settings
    }

    if testMode:
        cancelButton = browser.find_element("xpath", "//*[@value='Cancel']")
        cancelButton.click()
        log('Canceled ' + runName)
        log_run_to_file(runName, "Unstack Run", "Canceled (Test Mode)", settings_dict)
        time.sleep(timeBetween)
    else:
        log('Submitting ' + runName)
        log('')
        saveButton = browser.find_element("xpath", "//*[@value='Save']")
        saveButton.click()
        log_run_to_file(runName, "Unstack Run", "Submitted", settings_dict)
        time.sleep(timeBetween)
