import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# time between keypresses (0.25 is a known good number)
timeBetween = .025

def basicRun(prefix, suffix,\
             maxIterations, base, seat,\
             min_floor, min_ceiling, min_threshold_hour, min_threshold_minute,\
             normal_floor, normal_ceiling, normal_threshold_hour, normal_threshold_minute,\
             max_floor, max_ceiling, max_threshold_hour, max_threshold_minute,\
             browser, testMode, verbose, runNumber):
  if prefix == "":
    runName = base + "-" + seat + "_" + str(min_floor) + "-" + str(min_ceiling) + "-" + str(min_threshold_hour) + str(min_threshold_minute).zfill(2) + "__" + str(normal_floor) + "-" + str(normal_ceiling) + "-" + str(normal_threshold_hour) + str(normal_threshold_minute).zfill(2) + "__" + str(max_floor) + "-" + str(max_ceiling) + "-" + str(max_threshold_hour) + str(max_threshold_minute).zfill(2) + "_" + suffix
  else:
    runName = prefix + "_" + base + "-" + seat + "_" + str(min_floor) + "-" + str(min_ceiling) + "-" + str(min_threshold_hour) + str(min_threshold_minute).zfill(2) + "__" + str(normal_floor) + "-" + str(normal_ceiling) + "-" + str(normal_threshold_hour) + str(normal_threshold_minute).zfill(2) + "__" + str(max_floor) + "-" + str(max_ceiling) + "-" + str(max_threshold_hour) + str(max_threshold_minute).zfill(2) + "_" + suffix

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
  a[0].send_keys(Keys.TAB)

  a[4].send_keys(Keys.TAB) #basically go to the minute portion of the min open credit field (the hour portion is a[3] and the minute portion is a[4]). Then tab to highlight what ends up being a[5}.

  if verbose:
    print("normal credit window: " + "floor-" + str(normal_floor) + ", ceiling-" + str(normal_ceiling) + ", threshold-" + str(normal_threshold_hour) + ":" + str(normal_threshold_minute))
    print("min credit window: " + "floor-" + str(min_floor) + ", ceiling-" + str(min_ceiling) + ", threshold-" + str(min_threshold_hour) + ":" + str(min_threshold_minute))
    print("max credit window: " + "floor-" + str(max_floor) + ", ceiling-" + str(max_ceiling) + ", threshold-" + str(max_threshold_hour) + ":" + str(max_threshold_minute))

  #normal credit window
  a[5].send_keys(normal_floor)
  a[5].send_keys(Keys.TAB)
  a[6].send_keys(Keys.TAB)
  a[7].send_keys(normal_ceiling)
  a[7].send_keys(Keys.TAB)
  a[8].send_keys(Keys.TAB)
  a[9].send_keys(normal_threshold_hour)
  a[9].send_keys(Keys.TAB)
  a[10].send_keys(normal_threshold_minute)
  a[10].send_keys(Keys.TAB)

  #min credit window
  a[11].send_keys(min_floor)
  a[11].send_keys(Keys.TAB)
  a[12].send_keys(Keys.TAB)
  a[13].send_keys(min_ceiling)
  a[13].send_keys(Keys.TAB)
  a[14].send_keys(Keys.TAB)
  a[15].send_keys(min_threshold_hour)
  a[15].send_keys(Keys.TAB)
  a[16].send_keys(min_threshold_minute)
  a[16].send_keys(Keys.TAB)

  #max credit window
  a[17].send_keys(max_floor)
  a[17].send_keys(Keys.TAB)
  a[18].send_keys(Keys.TAB)
  a[19].send_keys(max_ceiling)
  a[19].send_keys(Keys.TAB)
  a[20].send_keys(Keys.TAB)
  a[21].send_keys(max_threshold_hour)
  a[21].send_keys(Keys.TAB)
  a[22].send_keys(max_threshold_minute)
  a[22].send_keys(Keys.TAB)

  time.sleep(timeBetween)


  # #####################################
  # ## Max credit window
  # #####################################
  # if verbose:
  #   print("max credit window: " + "floor-" + str(max_floor) + ", ceiling-" + str(max_ceiling) + ", threshold-" + str(max_threshold_hour) + ":" + str(max_threshold_minute))
  #
  #
  # a[17].send_keys(Keys.BACKSPACE)
  # a[17].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[17].send_keys(max_floor)
  # time.sleep(timeBetween)
  # a[17].send_keys(Keys.TAB)
  # time.sleep(5)
  #
  # a[19].send_keys(Keys.BACKSPACE)
  # a[19].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[19].send_keys(max_ceiling)
  # time.sleep(timeBetween)
  #
  # a[21].send_keys(Keys.BACKSPACE)
  # a[21].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # print("sending normal threshold hour of " + str(normal_threshold_hour))
  # a[21].send_keys(max_threshold_hour)
  # time.sleep(timeBetween)
  # a[21].send_keys(Keys.TAB)
  # a[22].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[22].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # if (max_threshold_minute > 40):
  #   a[22].send_keys("45")
  # elif (max_threshold_minute > 25):
  #   a[22].send_keys("30")
  # elif (max_threshold_minute > 10):
  #   a[22].send_keys("15")
  # else:
  #   a[22].send_keys("00")
  # time.sleep(timeBetween)
  # #a[22].send_keys(Keys.TAB)
  #
  # #####################################
  # ## Normal credit window
  # #####################################
  # if verbose:
  #   print("normal credit window: " + "floor-" + str(normal_floor) + ", ceiling-" + str(normal_ceiling) + ", threshold-" + str(normal_threshold_hour) + ":" + str(normal_threshold_minute))
  # a[5].send_keys(Keys.BACKSPACE)
  # a[5].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[5].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[5].send_keys(normal_floor)
  # time.sleep(timeBetween)
  #
  # a[7].send_keys(Keys.BACKSPACE)
  # a[7].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[7].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[7].send_keys(normal_ceiling)
  # time.sleep(timeBetween)
  #
  # time.sleep(.5)
  # a[9].send_keys(Keys.BACKSPACE)
  # a[9].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[9].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # print("sending normal threshold hour of " + str(normal_threshold_hour))
  # a[9].send_keys(normal_threshold_hour)
  # time.sleep(1)
  # a[9].send_keys(Keys.TAB)
  # a[10].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[10].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # if (normal_threshold_minute > 40):
  #   a[10].send_keys("45")
  # elif (normal_threshold_minute > 25):
  #   a[10].send_keys("30")
  # elif (normal_threshold_minute > 10):
  #   a[10].send_keys("15")
  # else:
  #   a[10].send_keys("00")
  # time.sleep(timeBetween)
  # a[10].send_keys(Keys.TAB)
  #
  # #####################################
  # ## Min credit window
  # #####################################
  # if verbose:
  #   print("min credit window: " + "floor-" + str(min_floor) + ", ceiling-" + str(min_ceiling) + ", threshold-" + str(min_threshold_hour) + ":" + str(min_threshold_minute))
  # a[11].send_keys(Keys.BACKSPACE)
  # a[11].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[11].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[11].send_keys(min_floor)
  # time.sleep(timeBetween)
  #
  # a[13].send_keys(Keys.BACKSPACE)
  # a[13].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[13].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[13].send_keys(min_ceiling)
  # time.sleep(timeBetween)
  #
  # time.sleep(.5)
  # a[15].send_keys(Keys.BACKSPACE)
  # a[15].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[15].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # print("sending normal threshold hour of " + str(normal_threshold_hour))
  # a[15].send_keys(min_threshold_hour)
  # time.sleep(1)
  # a[15].send_keys(Keys.TAB)
  # a[16].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[16].send_keys(Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # if (min_threshold_minute > 40):
  #   a[16].send_keys("45")
  # elif (min_threshold_minute > 25):
  #   a[16].send_keys("30")
  # elif (min_threshold_minute > 10):
  #   a[16].send_keys("15")
  # else:
  #   a[16].send_keys("00")
  # time.sleep(timeBetween)
  # a[16].send_keys(Keys.TAB)

  # a[23].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
  # time.sleep(timeBetween)
  # a[23].send_keys("50")
  # time.sleep(timeBetween)

  ####################################
  ## Cancel or save
  #####################################
  if testMode:
    cancelButton = browser.find_element_by_xpath("//*[@value='Cancel']")
    cancelButton.click()
    if verbose:
      print('Canceled ' + runName)
    time.sleep(timeBetween)
  else:
    if verbose:
      print('Submitting ' + runName)
      print()
    saveButton = browser.find_element_by_xpath("//*[@value='Save']")
    saveButton.click()
    time.sleep(timeBetween)