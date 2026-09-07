# Automated Test Runs
# TODO: Actually get it working...

from seleniumSetup import *
from browserSetup import *
from basicRun import *
from config import *

def testrun(date_time, browser):
    if baselineTest == "CA" or baselineTest == "All":
        basicRun("TEST_low", date_time, ten_mil, "IAH", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
                 verbose, 1)
        basicRun("TEST_low", date_time, ten_mil, "IAD", "CA", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
                 verbose, 2)
        basicRun("TEST_mid", date_time, ten_mil, "IAH", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
                 verbose, 3)
        basicRun("TEST_mid", date_time, ten_mil, "IAD", "CA", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
                 verbose, 4)
        basicRun("TEST_high", date_time, ten_mil, "IAH", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
                 verbose, 5)
        basicRun("TEST_high", date_time, ten_mil, "IAD", "CA", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
                 verbose, 6)
        basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90,
                 browser, testMode, verbose, 7)
        basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "CA", 85, 100, 90, 85, 100, 90, 85, 100, 90,
                 browser, testMode, verbose, 8)
    elif baselineTest == "FO" or baselineTest == "All":
        basicRun("TEST_low", date_time, ten_mil, "IAH", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
                 verbose, 1)
        basicRun("TEST_low", date_time, ten_mil, "IAD", "FO", 60, 75, 65, 70, 85, 75, 80, 95, 90, browser, testMode,
                 verbose, 2)
        basicRun("TEST_mid", date_time, ten_mil, "IAH", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
                 verbose, 3)
        basicRun("TEST_mid", date_time, ten_mil, "IAD", "FO", 70, 85, 75, 75, 90, 80, 80, 95, 90, browser, testMode,
                 verbose, 4)
        basicRun("TEST_high", date_time, ten_mil, "IAH", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
                 verbose, 5)
        basicRun("TEST_high", date_time, ten_mil, "IAD", "FO", 75, 90, 80, 80, 95, 85, 85, 100, 90, browser, testMode,
                 verbose, 6)
        basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAH", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90,
                 browser,
                 testMode, verbose, 7)
        basicRun("TEST_ridiculouslyhigh", date_time, ten_mil, "IAD", "FO", 85, 100, 90, 85, 100, 90, 85, 100, 90,
                 browser,
                 testMode, verbose, 8)
