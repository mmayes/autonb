from seleniumSetup import *
from browserSetup import *
from basicRun import *
from complexRun import *

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

# add a prefix to the run
# this can be useful if you want to label runs with "test"
# if it's empty between the quotes then nothing will be added
prefix = "test"

# add a suffix to the end of the name of the run
# this is useful if you already did a set of runs so this will be added to the end to make it unique
# if it's empty between the quotes then nothing will be added
# not really necessary since timestamps are included
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

browser = seleniumSetup()
browserSetup(browser, productionServer)
time.sleep(5) #wait for the javascript to load

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
                                                    basicRun(prefix, date_time, ten_mil, base, seat, minFloor, minCeiling, minThresholdHour, minThresholdMinute, normalFloor, normalCeiling, normalThresholdHour, normalThresholdMinute, maxFloor, maxCeiling, maxThresholdHour, maxThresholdMinute, browser, testMode, verbose, runcount)
                                                else:
                                                    print("skipping run " + str(runcount) + " because min threshold is greater than normal threshold")
                                            else:
                                                print("skipping run " + str(runcount) + " because normal threshold is greater than max threshold")
                                        else:
                                            print("skipping run " + str(runcount) + " because normal floor is greater than max floor")
                                    else:
                                        print("skipping run " + str(runcount) + " because min floor is greater than normal floor")
                        runcount = runcount + 1

print ('**************')
print('Runs complete')
print ('**************')