from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os
from selenium.webdriver.common.action_chains import ActionChains

class UpdateTimeZone(unittest.TestCase):
    def setUp(self):
        chromedriver = "/usr/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        # driver = webdriver.InternetExplorerDriver();
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://community.teamcomcast.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

  
    def test_update_time_zone(self):
        driver = self.driver
        driver.get(self.base_url + "/i/a3/NBW/Lists/Realtime%20Reports/AllItems.aspx")
        time.sleep(10)
        driver.maximize_window()
        homeHandle = driver.window_handles[0]
        time.sleep(8)
        # driver.find_element_by_link_text("360 Net").click()
        carriers = driver.find_elements_by_xpath("//a[contains(@href, '/i/a3/NBW/SitePages/')]")
        print len(carriers[17:])
        print carriers
        for carrier in carriers[14:]:
            print carrier.get_attribute('href')
        #     body = driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        #     # ActionChains(driver).send_keys(Keys.COMMAND, "t").perform()
        #     print "Opened tab"
        #     # time.sleep(1)
        #     body.send_keys(Keys.CONTROL + 'l')
        #     # time.sleep(1)
        #     body.send_keys(carrier.get_attribute('href'))
        #     # time.sleep(1)
        #     body.send_keys(Keys.E
        #         NTER)
        #     time.sleep(1)
        #     # time.sleep(1)
        #     # body.send_keys(Keys.CONTROL + '1')
        #     # driver.switch_to_window(homeHandle)
        # time.sleep(60)
        # print len(driver.window_handles), "Num Handles"
        # for i in xrange(len(carriers)):
            # print i, "- i"
            # driver.switch_to_window(driver.window_handles[i+1])
            # body.send_keys(Keys.CONTROL + str(i+1-14))
            def find_by_jquery(driver, jquery_selector):
                """Injects JQuery into the page.  This will allow the page to accept jquery javascript
                commands for automating some of the items selenium may have troubles with.
                @param webdriver_or_page_object: Selenium webdriver or a WTF PageObject."""
                jquery = open('jquery.min.js').read()
                driver.execute_script(jquery)
                javascript = "return $(\"{0}\")[0]".format(jquery_selector)
                return driver.execute_script(javascript)
            carrier.click()
            time.sleep(8)
            driver.find_element_by_css_selector("img[alt=\"Edit\"]").click()
            time.sleep(5)
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='Ribbon.EditingTools.CPEditTab.Markup.Html-Medium']/span[1]").click()
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='Ribbon.EditingTools.CPEditTab.Markup.Html.Menu.Html.EditSource-Menu16']/span[3]").click()
            time.sleep(5)
            driver.switch_to_default_content()
            print driver.find_element_by_xpath("/html/body/iframe").location
            print driver.find_element_by_xpath("/html/body/iframe").size
            # driver.switch_to_frame(driver.find_element_by_css_selector("body > iframe:nth-child(24)"))
            # elem = driver.find_element_by_xpath("/html/body/iframe")


            # secondIframe = find_by_jquery(driver, "#DlgFrame157961cb-7fda-4d46-b93f-dab096e0eee7")
            # print "The PE is: ", PE_cell.text
            # driver.switch_to_frame(secondIframe)
            # children = secondIframe.find_elements_by_xpath("./*")
            time.sleep(10)
            driver.switch_to_frame(driver.find_element_by_xpath("//*[contains(@id,'DlgFrame')]"))
            # driver.switch_to_frame(driver.find_element_by_xpath("/html/body/iframe"))       
            # print children

            # time.sleep(5)
            # # text = driver.find_element_by_css_selector("PropertyEditor").get_attribute('value')

            # text = driver.find_element_by_xpath("//*[@id='PropertyEditor']").get_attribute("value")
            # print text
            # time.sleep(5)
            driver.find_element_by_xpath("//*[@id='CancelButton']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//a[@id='Ribbon.EditingTools.CPEditTab.EditAndCheckout.SaveEdit-SelectedItem']/span/span/img").click()
            time.sleep(5)
            driver.find_element_by_id("ctl00_PlaceHolderMain_btnWikiSave").click()
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='zz18_V4QuickLaunchMenu']/div/ul/li[2]/ul/li[6]/a/span/span").click()
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='zz21_V4QuickLaunchMenu']/div/ul/li[2]/ul/li[6]/a/span/span[1]")
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    