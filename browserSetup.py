def browserSetup(browser, productionServer):
    if productionServer:
        # browser.get('https://transstates.navtechpbs.com/cgi-bin-xml/class/login.cgi')
        browser.get('https://ucapbs.navblue.aero/cgi-bin-xml/class/login.cgi')
        try:
            empNum = browser.find_element_by_name('EmployeeNumber')
            empNum.send_keys('######')
            passwordElem = browser.find_element_by_name('Password')
            passwordElem.send_keys('######')
            passwordElem.submit()
            print('Logged in')
            print()
        except:
            print('Might already be logged in')
    else:
        browser.get('https://transstatesuat.navtechpbs.com/cgi-bin-xml/class/login.cgi')
        try:
            empNum = browser.find_element_by_name('EmployeeNumber')
            empNum.send_keys('######')
            passwordElem = browser.find_element_by_name('Password')
            passwordElem.send_keys('######')
            passwordElem.submit()
            print('Logged in')
            print()
        except:
            print('Might already be logged in')