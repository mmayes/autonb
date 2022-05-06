import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# time between keypresses (0.25 is a known good number)
timeBetween = .025

def basicRun(prefix, suffix,\
             maxIterations, base, seat,\
             min_floor, min_ceiling, min_threshold,\
             normal_floor, normal_ceiling, normal_threshold,\
             max_floor, max_ceiling, max_threshold,\
             browser, testMode, verbose, runNumber):
  if prefix == "":
    runName = base + "-" + seat + "_" + str(min_floor) + "-" + str(min_ceiling) + "-" + str(min_threshold) + "__" + str(normal_floor) + "-" + str(normal_ceiling) + "-" + str(normal_threshold) + "__" + str(max_floor) + "-" + str(max_ceiling) + "-" + str(max_threshold) + "_" + suffix
  else:
    runName = prefix + "_" + base + "-" + seat + "_" + str(min_floor) + "-" + str(min_ceiling) + "-" + str(min_threshold) + "__" + str(normal_floor) + "-" + str(normal_ceiling) + "-" + str(normal_threshold) + "__" + str(max_floor) + "-" + str(max_ceiling) + "-" + str(max_threshold) + "_" + suffix
  print("starting run " + str(runNumber) + ": " + runName)

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
  # if verbose:
  #   #prints a log of all the ValidatingText elements
  #   print(len(a))
  #   for element in a:
  #     print("element = ", element.get_attribute("id"), " with value ", element.get_attribute("value"))

  #####################################
  ## Max Iterations
  #####################################
  if verbose:
    print("max iterations: " + str(maxIterations))
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

  time.sleep(1)
  a[21].send_keys(Keys.BACKSPACE)
  a[21].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[21].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[21].send_keys(max_threshold)
  time.sleep(timeBetween)
  a[21].send_keys(Keys.TAB)

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

  time.sleep(1)
  a[9].send_keys(Keys.BACKSPACE)
  a[9].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[9].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[9].send_keys(normal_threshold)
  time.sleep(timeBetween)
  a[9].send_keys(Keys.TAB)

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

  time.sleep(1)
  a[15].send_keys(Keys.BACKSPACE)
  a[15].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[15].send_keys(Keys.BACKSPACE)
  time.sleep(timeBetween)
  a[15].send_keys(min_threshold)
  time.sleep(timeBetween)
  a[15].send_keys(Keys.TAB)

  # a[23].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[23].send_keys("50")
  # time.sleep(timeBetween)

  ####################################
  ## Cancel or save
  #####################################
  time.sleep(1)
  if testMode:
    #time.sleep(3)
    cancelButton = browser.find_element_by_xpath("//*[@value='Cancel']")
    cancelButton.click()
    if verbose:
      print('Canceled ' + runName)
    time.sleep(0.05)
  else:
    if verbose:
      print('Submitting ' + runName)
      print()
    saveButton = browser.find_element_by_xpath("//*[@value='Save']")
    saveButton.click()
    time.sleep(0.5)