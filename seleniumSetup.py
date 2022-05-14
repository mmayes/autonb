from selenium import webdriver

def seleniumSetup():
    browser = webdriver.Chrome('/usr/local/bin/chromedriver') #might have to point to a different location

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()
    return browser
