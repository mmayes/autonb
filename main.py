import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from basicRun import *
from complexRun import *
from browserSetup import *

# set the seat to either 'CA' or 'FO'
seat = 'CA'

# set the base as individual or group of bases
# group would be separated by comma like this: baseList = ['DEN','ORD','STL']
# individual would be baseList = ['STL']
baseList = ['IAH']

# set the max number of people that can bid min credit
# contractually limited to 10% of line holders for a given base and position
# set to 0 if number of min credit bidders will not be restricted
maxMinCredit = 0

# add a suffix to the end of the name of the run
# this is useful if you already did a set of runs so this will be added to the end to make it unique
# if it's empty between the quotes then nothing will be added
suffix = ""

# set the max stack height for unstacking on line holders
# maximimum stack height must be at least 6% of regular line holders
# for holidays, contractually limited to 50% of regular pilots (does not specify line holders so I interpret to mean bidding pilots)
# set to 0 if line holders will not be unstacked on
unstackLineHolders = 0
maxPasses = 20
pointOrDayStack = "day" #set this to either "point" or "day"

# set the max number of iterations
# Our default is set to 2,000,000. Help file says it should be between 5,000,000 and 10,000,000
two_mil = 2000000
five_mil = 5000000
ten_mil = 10000000
all_nines = 99999999
# maxIterations = 2000000
# maxIterations = 5000000
maxIterations = 10000000
# maxIterations = 99999999

# specify which server and credentials to use
# using the production server is normal and would be set to True
productionServer = True

# check each base to get a baseline
# can be set to "All", "None", "CA", or "FO"
# NOTE: if All is selected, the FO runs will possibly be based off of runs prior to the latest captain runs being complete
baselineTest = "None"

# set the testMode to True or False.
# If set to True, the program will go through the motions, but not actually start the run
testMode = False

# print detailed messages
verbose = False

# time between keypresses (0.25 is a known good number)
timeBetween = 0.025

browser = webdriver.Chrome()
#browser = webdriver.Safari()
#browser.maximize_window()

time.sleep(5) #wait for the javascript to load
browserSetup(browser, productionServer)

runcount = 1
now = datetime.now()  # current date and time
date_time = now.strftime("%Y-%m-%d_%H:%M:%S")

if baselineTest == "CA" or baselineTest == "All":
    basicRun("TEST_low", date_time, ten_mil, "IAH", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,1)
    basicRun("TEST_low", date_time, ten_mil, "DEN", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,2)
    basicRun("TEST_low", date_time, ten_mil, "IAD", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,3)
    basicRun("TEST_low", date_time, ten_mil, "EWR", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,4)
    basicRun("TEST_mid", date_time, ten_mil, "IAH", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,5)
    basicRun("TEST_mid", date_time, ten_mil, "DEN", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,6)
    basicRun("TEST_mid", date_time, ten_mil, "IAD", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,7)
    basicRun("TEST_mid", date_time, ten_mil, "EWR", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,8)
    basicRun("TEST_high", date_time, ten_mil, "IAH", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,9)
    basicRun("TEST_high", date_time, ten_mil, "DEN", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,10)
    basicRun("TEST_high", date_time, ten_mil, "IAD", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,11)
    basicRun("TEST_high", date_time, ten_mil, "EWR", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,12)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose,13)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "DEN", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose,14)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose,15)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "EWR", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose,16)
elif baselineTest == "FO" or baselineTest == "All":
    basicRun("TEST_low", date_time, ten_mil, "IAH", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,1)
    basicRun("TEST_low", date_time, ten_mil, "DEN", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,2)
    basicRun("TEST_low", date_time, ten_mil, "IAD", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,3)
    basicRun("TEST_low", date_time, ten_mil, "EWR", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode, verbose,4)
    basicRun("TEST_mid", date_time, ten_mil, "IAH", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,5)
    basicRun("TEST_mid", date_time, ten_mil, "DEN", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,6)
    basicRun("TEST_mid", date_time, ten_mil, "IAD", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,7)
    basicRun("TEST_mid", date_time, ten_mil, "EWR", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode, verbose,8)
    basicRun("TEST_high", date_time, ten_mil, "IAH", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,9)
    basicRun("TEST_high", date_time, ten_mil, "DEN", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,10)
    basicRun("TEST_high", date_time, ten_mil, "IAD", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,11)
    basicRun("TEST_high", date_time, ten_mil, "EWR", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode, verbose,12)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose, 13)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "DEN", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose, 14)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose, 15)
    basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "EWR", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90, browser, testMode, verbose, 16)
else:
    for base in baseList:
        #set the constants for fixed windows
        minFloor = 65
        minCeiling = 80
        normalFloor = 70
        normalCeiling = 85
        maxFloor = 75
        maxCeiling = 90
        for minThresholdHour in range(minFloor, minCeiling, 3): #incrememnt the threshold hour between the floor and ceiling
            for minThresholdMinute in range(0, 60, 60): #set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                for maxThresholdHour in range(maxFloor, maxCeiling, 3): #incrememnt the threshold hour between the floor and ceiling
                    for maxThresholdMinute in range(0, 60, 60): #set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                        for normalThresholdHour in range(normalFloor, normalCeiling): #incrememnt the threshold hour between the floor and ceiling
                            for normalThresholdMinute in range(0, 60, 30): #set the minute portion of the threshold. If set to (0, 60, 60) it will just do whole hours. If set to (0, 60, 30) then it will be 30 min increments. Can go as low as 15 minute increments.
                                    if minFloor <= normalFloor: #NAVBLUE won't let the min floor be greater than the normal floor
                                        if normalFloor <= maxFloor: #NAVBLUE won't let the normal floor be greater than the max floor
                                            # we don't want the normal threshold to ever be greater than max threshold. They can be equal though.
                                            if ((normalThresholdHour < maxThresholdHour) or ((normalThresholdHour == maxThresholdHour) and (normalThresholdMinute <= maxThresholdMinute))):
                                                # we don't want the min threshold to ever be greater than normal threshold. They can be equal though.
                                                if ((minThresholdHour < normalThresholdHour) or ((minThresholdHour == normalThresholdHour) and (minThresholdMinute <= normalThresholdMinute))):
                                                    basicRun("", date_time, ten_mil, base, seat, minFloor, minCeiling, minThresholdHour, minThresholdMinute, normalFloor, normalCeiling, normalThresholdHour, normalThreshholdMinute, maxFloor, maxCeiling, maxThresholdHour, maxThresholdMinute, browser, testMode, verbose, runcount)
                                                else:
                                                    print("skipping run " + str(runcount) + " because min threshold is greater than normal threshold")
                                            else:
                                                print("skipping run " + str(runcount) + " because normal threshold is greater than max threshold")
                                        else:
                                            print("skipping run " + str(runcount) + " because normal floor is greater than max floor")
                                    else:
                                        print("skipping run " + str(runcount) + " because min floor is greater than normal floor")
                        runcount = runcount + 1
                    # we don't want the normal threshold to ever be greater than max threshold. They can be equal though.
                    # if ((normThresholdHour < maxThresholdHour) or ((normThresholdHour == maxThresholdHour) and (normThresholdMinute <= maxThresholdMinute))):
                    # if not ((maxThresholdHour == normThresholdHour) and (normThresholdMinute > maxThresholdMinute)):


# for base in baseList:
#     for minThresholdHour in range(75, 79, 3):  # typical range for min credit runs 75 and 78
#         for minThresholdMinute in range(0, 60, 60):
#             for maxThresholdHour in range(85, 92, 3):  # typical range for max credit runs 85, 88, 91
#                 for maxThresholdMinute in range(0, 60, 60):
#                     for normThresholdHour in range(80, 86):  # typical range for normal credit 81, 82, 83, 84, 85
#                         for normThresholdMinute in range(0, 60, 30):
#                             runName = "test_" + base + "-" + seat + "_" + str(minThresholdHour) + str(minThresholdMinute).zfill(
#                                 2) + "_" + str(normThresholdHour) + str(normThresholdMinute).zfill(2) + "_" + str(
#                                 maxThresholdHour) + str(maxThresholdMinute).zfill(2)
#                             # if number of minCredit bidders is restricted then it will be greater than 0. So add that to the name of the run
#                             if (maxMinCredit > 0):
#                                 runName = runName + "-MC" + str(maxMinCredit)
#                             # if (maxIterations > 2000000):
#                             #	runName = runName + "-MI"
#                             if (unstackLineHolders > 0):
#                                 if pointOrDayStack == "day":
#                                     runName = runName + "-USLD" + str(unstackLineHolders)
#                                 else:
#                                     runName = runName + "-USLP" + str(unstackLineHolders)
#                             runName = runName + suffix
#                             # we don't want the normal threshold to ever be greater than max threshold. They can be equal though.
#                             if ((normThresholdHour < maxThresholdHour) or ((normThresholdHour == maxThresholdHour) and (
#                                     normThresholdMinute <= maxThresholdMinute))):
#                                 # if not ((maxThresholdHour == normThresholdHour) and (normThresholdMinute > maxThresholdMinute)):
#                                 try:
#                                     element = WebDriverWait(browser, 60).until(
#                                         EC.visibility_of_element_located((By.XPATH, "//*[@value='Launch Run']"))
#                                     )
#                                     print("Launch page is ready")
#                                     launchButton = browser.find_element_by_xpath("//*[@value='Launch Run']")
#                                     launchButton.click()
#                                 except:
#                                     print('Took too long to load javascript')
#
#                                 time.sleep(3)
#                                 print('Starting ' + runName)
#
#                                 try:
#                                     groupDropdown = Select(browser.find_element_by_xpath(
#                                         "//*[contains(@id,'add_run_to_queue_rungroups')]"))
#                                     #group = base + "-EMB-" + seat
#                                     group = base + "-XMJ-" + seat
#                                     groupDropdown.select_by_visible_text(group)
#                                 except:
#                                     print('Problem with group dropdown')
#
#                                 # set the run name
#                                 try:
#                                     runNameTextBox = browser.find_element_by_xpath(
#                                         "//*[contains(@id,'add_run_to_queue_name')]")
#                                     runNameTextBox.send_keys(runName)
#                                 except:
#                                     print('Problem with Run Name textbox')
#
#                                 #							try:
#                                 #								element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select.List")))
#                                 #								print ("list is ready")
#                                 #							except:
#                                 #								print('Took too long to load list')
#
#                                 a = []
#                                 a = browser.find_elements_by_class_name("ValidatingText")
#
#                                 if testMode:
#                                     # prints a log of all the ValidatingText elements
#                                     print(len(a))
#                                     for element in a:
#                                         print("element = ", element.get_attribute("id"), " with value ", element.get_attribute("value"))
#
#                                 #####################################
#                                 ## Max Iterations
#                                 #####################################
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[0].send_keys(maxIterations)
#
#                                 #####################################
#                                 ## Credit windows
#                                 #####################################
#
#                                 a[21].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[21].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[21].send_keys(maxThresholdHour)
#                                 time.sleep(timeBetween)
#                                 a[22].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[22].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 if (maxThresholdMinute > 0):
#                                     a[22].send_keys(maxThresholdMinute)
#                                 else:
#                                     a[22].send_keys("00")
#                                 time.sleep(timeBetween)
#
#                                 a[9].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[9].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[9].send_keys(normThresholdHour)
#                                 time.sleep(timeBetween)
#                                 a[10].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[10].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 if (normThresholdMinute > 40):
#                                     # a[10].send_keys(maxThresholdMinute)
#                                     a[10].send_keys("45")
#                                 elif (normThresholdMinute > 25):
#                                     a[10].send_keys("30")
#                                 elif (normThresholdMinute > 10):
#                                     a[10].send_keys("15")
#                                 else:
#                                     a[10].send_keys("00")
#                                 time.sleep(timeBetween)
#
#                                 a[15].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[15].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[15].send_keys(minThresholdHour)
#                                 time.sleep(timeBetween)
#                                 a[16].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 a[16].send_keys(Keys.BACKSPACE)
#                                 time.sleep(timeBetween)
#                                 if (minThresholdMinute > 0):
#                                     a[16].send_keys(maxThresholdMinute)
#                                 else:
#                                     a[16].send_keys("00")
#                                 time.sleep(timeBetween)
#
#                                 ############################################################
#                                 ## Set the max number of people that can bid min credit
#                                 ############################################################
#
#                                 # set the max number of people that can bid min credit
#                                 if maxMinCredit > 0:
#                                     a[23].send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
#                                     time.sleep(timeBetween)
#                                     a[23].send_keys(maxMinCredit)
#                                     time.sleep(timeBetween)
#
#                                 #####################################
#                                 ## Split duty items
#                                 #####################################
#
#                                 #								#set the low end of the split duty to 75 hours to match the normal window
#                                 #								a[24].send_keys(Keys.TAB)
#                                 #								a[25].send_keys(75)
#                                 #								a[25].send_keys(Keys.TAB)
#                                 #								time.sleep(1)
#                                 #								a[26].send_keys(Keys.TAB)
#                                 #
#                                 #								#set the high end of the split duty to 95 hours to match the normal window
#                                 #								a[27].send_keys(95)
#                                 #								a[27].send_keys(Keys.TAB)
#                                 #								time.sleep(1)
#                                 #								a[28].send_keys(Keys.TAB)
#                                 #
#                                 #								#set the threshold of the split duty to match the normal window threshold
#                                 #								a[29].send_keys(normThresholdHour)
#                                 #								a[29].send_keys(Keys.TAB)
#                                 #								a[30].send_keys(normThresholdMinute)
#                                 #								a[30].send_keys(Keys.TAB)
#                                 #								a[31].send_keys(Keys.TAB)
#                                 #


print ('**************')
print('Runs complete')
print ('**************')