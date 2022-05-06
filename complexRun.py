import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# time between keypresses (0.25 is a known good number)
timeBetween = 0.001

def complexRun(browser, testMode, prefix, suffix, maxIterations, base, seat, min_floor_hour, min_floor_minutes, min_ceiling_hour, min_ceiling_minutes, min_threshold_hour, min_threshold_minutes, normal_floor_hour, normal_floor_minutes, normal_ceiling_hour, normal_ceiling_minutes, normal_threshold_hour, normal_threshold_minutes,max_floor_hour, max_floor_minutes, max_ceiling_hour, max_ceiling_minutes, max_threshold_hour, max_threshold_minutes):
  runName = prefix + "_" + base + "-" + seat + "_" + str(min_floor_hour) + str(min_floor_minutes.zfill(2)) + "-" + str(min_ceiling_hour) + str(min_ceiling_minutes.zfill(2)) + "-" + str(min_threshold_hour) + str(min_threshold_minutes.zfill(2)) + "_" + str(normal_floor_hour) + str(normal_floor_minutes.zfill(2)) + "-" + str(normal_ceiling_hour) + str(normal_ceiling_minutes.zfill(2)) + "-" + str(normal_threshold_hour) + str(normal_threshold_minutes.zfill(2)) + "_" + str(max_floor_hour) + str(max_floor_minutes.zfill(2)) + "-" + str(max_ceiling_hour) + str(max_ceiling_minutes.zfill(2)) + "-" + str(max_threshold_hour) + str(max_threshold_minutes.zfill(2)) + "_" + suffix
  print("starting: " + runName)

  element = WebDriverWait(browser, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@value='Launch Run']"))
  )
  if verbose:
    print("Launch page is ready")
  launchButton = browser.find_element_by_xpath("//*[@value='Launch Run']")
  launchButton.click()

  groupDropdown = Select(browser.find_element_by_xpath(
    "//*[contains(@id,'add_run_to_queue_rungroups')]"))
  # group = base + "-EMB-" + seat
  group = base + "-XMJ-" + seat
  if verbose:
    print("selecting " + group)
  groupDropdown.select_by_visible_text(group)

  # set the run name
  runNameTextBox = browser.find_element_by_xpath(
    "//*[contains(@id,'add_run_to_queue_name')]")
  runNameTextBox.send_keys(runName)

  a = []
  a = browser.find_elements_by_class_name("ValidatingText")
  if verbose:
    #prints a log of all the ValidatingText elements
    print(len(a))
    for element in a:
      print("element = ", element.get_attribute("id"), " with value ", element.get_attribute("value"))

  #####################################
  ## Max Iterations
  #####################################
  if verbose:
    print("max iterations: " + str(maxIterations))
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[0].send_keys(maxIterations)

  #####################################
  ## Normal credit window
  #####################################
  if verbose:
    print("normal credit window: " + "floor-" + str(normal_floor) + ", ceiling-", str(normal_ceiling) + ", threshold-" + str(normal_threshold))
  a[5].send_keys(Keys.BACKSPACE)
  a[5].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[5].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[5].send_keys(normal_floor)
  time.sleep(timeBetween)

  a[7].send_keys(Keys.BACKSPACE)
  a[7].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[7].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[7].send_keys(normal_ceiling)
  time.sleep(timeBetween)

  a[9].send_keys(Keys.BACKSPACE)
  a[9].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[9].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[9].send_keys(normal_threshold)
  time.sleep(timeBetween)

  #####################################
  ## Min credit window
  #####################################
  if verbose:
    print("min credit window: " + "floor-" + str(min_floor) + ", ceiling-", str(min_ceiling) + ", threshold-" + str(min_threshold))
  a[11].send_keys(Keys.BACKSPACE)
  a[11].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[11].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[11].send_keys(min_floor)
  time.sleep(timeBetween)

  a[13].send_keys(Keys.BACKSPACE)
  a[13].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[13].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[13].send_keys(min_ceiling)
  time.sleep(timeBetween)

  a[15].send_keys(Keys.BACKSPACE)
  a[15].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[15].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[15].send_keys(min_threshold)
  time.sleep(timeBetween)

  #####################################
  ## Max credit window
  #####################################
  if verbose:
    print("max credit window: " + "floor-" + str(max_floor) + ", ceiling-", str(max_ceiling) + ", threshold-" + str(max_threshold))
  a[17].send_keys(Keys.BACKSPACE)
  a[17].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[17].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[17].send_keys(max_floor)
  time.sleep(timeBetween)

  a[19].send_keys(Keys.BACKSPACE)
  a[19].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[19].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[19].send_keys(max_ceiling)
  time.sleep(timeBetween)

  a[21].send_keys(Keys.BACKSPACE)
  a[21].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[21].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[21].send_keys(max_threshold)
  time.sleep(timeBetween)





  #                                 # #####################################
  #                                 # ## Unstack on line holders
  #                                 # #####################################
  #                                 # if unstackLineHolders > 0:
  #                                 #     listOfCheckBoxes = []
  #                                 #     listOfCheckBoxes = browser.find_elements_by_class_name("CheckBox")
  #                                 #
  #                                 #     # the unstack on lineholder checkbox is the third checkbox in the array
  #                                 #     listOfCheckBoxes[2].click()
  #                                 #     time.sleep(timeBetween)
  #                                 #
  #                                 #     if verbose:
  #                                 #         # prints a log of all the checkboxes
  #                                 #         print("\nCheckboxes")
  #                                 #         print(len(listOfCheckBoxes))
  #                                 #         for element in listOfCheckBoxes:
  #                                 #             print("checkbox = ", element.get_attribute("id"), " with value ",
  #                                 #                   element.get_attribute("value"))
  #                                 #
  #                                 #     # set number of max passes
  #                                 #     try:
  #                                 #         a[49].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #         time.sleep(timeBetween)
  #                                 #         a[49].send_keys(maxPasses)
  #                                 #         time.sleep(timeBetween)
  #                                 #     except:
  #                                 #         print('Issue with the max passes text box')
  #                                 #
  #                                 #     listOfRadioButtons = []
  #                                 #     listOfRadioButtons = browser.find_elements_by_class_name("RadioButton")
  #                                 #     if pointOrDayStack == "day":
  #                                 #         listOfRadioButtons[1].click()
  #                                 #
  #                                 #     if verbose:
  #                                 #         print("\nRadio Buttons")
  #                                 #         # prints a log of all the radio buttons
  #                                 #         print(len(listOfRadioButtons))
  #                                 #         for element in listOfRadioButtons:
  #                                 #             print("radiobutton = ", element.get_attribute("id"), " with value ",
  #                                 #                   element.get_attribute("value"))
  #                                 #
  #                                 #     # # check the priority stack date box which is the fifth checkbox in the array
  #                                 #     # listOfCheckBoxes[4].click()
  #                                 #     # time.sleep(timeBetween)
  #                                 #     #
  #                                 #     # listOfDropdowns = []
  #                                 #     # listOfDropdowns = browser.find_elements_by_class_name("DropDownList")
  #                                 #     #
  #                                 #     # # select the month for the priority stack date. This is the fifth dropdown in the array
  #                                 #     # monthDropdown = Select(listOfDropdowns[4])
  #                                 #     # monthDropdown.select_by_visible_text("December")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # select the day for the priority stack date. This is the sixth dropdown in the array
  #                                 #     # dayDropdown = Select(listOfDropdowns[5])
  #                                 #     # dayDropdown.select_by_visible_text("25")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     #
  #                                 #     # if verbose:
  #                                 #     #     # prints a log of all the dropdown lists
  #                                 #     #     print(len(listOfDropdowns))
  #                                 #     #     for element in listOfDropdowns:
  #                                 #     #         print("dropdown = ", element.get_attribute("id"), " with value ",
  #                                 #     #               element.get_attribute("value"))
  #                                 #
  #                                 #     # set the max stack height for each day
  #                                 #     # # day 1
  #                                 #     # a[52].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[52].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 2
  #                                 #     # a[53].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[53].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 3
  #                                 #     # a[54].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[54].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 4
  #                                 #     # a[55].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[55].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 5
  #                                 #     # a[56].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[56].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 6
  #                                 #     # a[57].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[57].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 7
  #                                 #     # a[58].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[58].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 8
  #                                 #     # a[59].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[59].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 9
  #                                 #     # a[60].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[60].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 10
  #                                 #     # a[61].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[61].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 11
  #                                 #     # a[62].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[62].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 12
  #                                 #     # a[63].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[63].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 13
  #                                 #     # a[64].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[64].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 14
  #                                 #     # a[65].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[65].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # day 15
  #                                 #     # a[66].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[66].send_keys("14")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 16
  #                                 #     # a[67].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[67].send_keys("10")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 17
  #                                 #     # a[68].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[68].send_keys("10")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 18
  #                                 #     # a[69].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[69].send_keys("12")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 19
  #                                 #     # a[70].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[70].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 20
  #                                 #     # a[71].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[71].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 21
  #                                 #     # a[72].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[72].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 22
  #                                 #     # a[73].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[73].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 23
  #                                 #     # a[74].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[74].send_keys("20")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 24
  #                                 #     # a[75].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[75].send_keys("5")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # day 25
  #                                 #     a[76].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     time.sleep(timeBetween)
  #                                 #     a[76].send_keys("18")
  #                                 #     time.sleep(timeBetween)
  #                                 #     # day 26
  #                                 #     a[77].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     time.sleep(timeBetween)
  #                                 #     a[77].send_keys("19")
  #                                 #     time.sleep(timeBetween)
  #                                 #     # day 27
  #                                 #     a[78].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     time.sleep(timeBetween)
  #                                 #     a[78].send_keys("19")
  #                                 #     time.sleep(timeBetween)
  #                                 #     # day 28
  #                                 #     # a[79].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[79].send_keys("12")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 29
  #                                 #     # a[80].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[80].send_keys("10")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 30
  #                                 #     # a[81].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[81].send_keys("10")
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # # day 31
  #                                 #     # a[82].send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
  #                                 #     # time.sleep(timeBetween)
  #                                 #     # a[82].send_keys("20")
  #                                 #     # time.sleep(timeBetween)

  ####################################
  ## Cancel or save
  #####################################
  if testMode:
    time.sleep(3)
    cancelButton = browser.find_element_by_xpath("//*[@value='Cancel']")
    cancelButton.click()
    if verbose:
      print('Canceled ' + runName)
    time.sleep(1)
  else:
    if verbose:
      print('Submitting ' + runName)
      print()
    saveButton = browser.find_element_by_xpath("//*[@value='Save']")
    saveButton.click()
    time.sleep(1)