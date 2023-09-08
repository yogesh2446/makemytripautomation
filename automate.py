import time
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from constants import *


date = datetime.datetime.now()
day = date.day
month = date.month
year = date.year
# month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

# URL = "http://www.makemytrip.com"
# RADIO_BUTTON_ID = 'round_trip_button1'
# MAKE_MY_TRIP = 'MakeMyTrip'
# FROM_INPUT_ID = 'from_typeahead1'
# TO_INPUT_ID = 'to_typeahead1'
# DEPART_DATE_ID = 'start_date_sec'
# RETURN_DATE_ID = 'return_date_sec'
# FROM_CITY = 'BLR'
# TO_CITY = 'DEL'
# DATEPICKER_MONTH_XPATH ='//*[@id="ui-datepicker-div"]/div[2]/div/div/span[1]'
# DATEPICKER_YEAR_XPATH = '//*[@id="ui-datepicker-div"]/div[2]/div/div/span[2]'
# SEARCH_BUTTON_ID = "flights_submit"
# MODAL_DIALOG_CLASS = 'modal-dialog'
# BOOK_BUTTON_FOOTER_CSS = 'span.clearfix > a'
# CONFIRM_MODAL_DIALOG_ID = 'fcModalBody'

class mmtAutomation(unittest.TestCase):

    def setUp(self):
        """
        Setup class for test cases in mmtAutomation Class
        """
        firefox_profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    # def tearDown(self):
        # driver = self.driver
        # driver.close()

    # def test_001_load_webpage(self):
        
        # try:
            # driver = self.driver
            # driver.get(URL)
            # self.assertTrue(MAKE_MY_TRIP in driver.title)
        
        # except Exception as e:
            # print e
    
    def test_001_Search_Flight(self):
        try:
            driver = self.driver
            driver.get(URL)
            
            radioButton = driver.find_element_by_id(RADIO_BUTTON_ID)
            radioButton.click()
            
            fromField = driver.find_element_by_id(FROM_INPUT_ID)
            fromField.send_keys(Keys.BACKSPACE)
            fromField.send_keys(FROM_CITY)
            # fromField.sendKeys(Keys.TAB)
            
            toField = driver.find_element_by_id(TO_INPUT_ID)
            toField.send_keys(Keys.BACKSPACE)
            toField.send_keys(TO_CITY)
            
            departDateField = driver.find_element_by_id(DEPART_DATE_ID)
            departDateField.click()
            driver.find_element_by_link_text("%s" % day).click()
            
            returnDateField = driver.find_element_by_id(RETURN_DATE_ID)
            returnDateField.click()
            driver.find_element_by_link_text("%s" % (day+1)).click()
            
            search_button = driver.find_element_by_id(SEARCH_BUTTON_ID)
            search_button.click()
            time.sleep(5)
            
            modal_dialog = driver.find_element_by_class_name(MODAL_DIALOG_CLASS)
            
            if modal_dialog:
                driver.find_element_by_link_text('Search Flight').click()
            
            # time.sleep(3)
            
            book_button_footer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, BOOK_BUTTON_FOOTER_CSS)))
            
            book_button_footer.click()
            
            try:
                # confirm_modal_dialog = driver.find_element_by_id(CONFIRM_MODAL_DIALOG_ID)
                confirm_modal_dialog = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, CONFIRM_MODAL_DIALOG_ID)))
                driver.find_element_by_link_text('Continue to Book').click()
            except:
                pass
            
            # MONTH = driver.find_element_by_xpath(DATEPICKER_MONTH_XPATH)
            # YEAR = driver.find_element_by_xpath(DATEPICKER_YEAR_XPATH)
        
        except Exception as e:
            print e
    
if __name__ == "__main__":
    unittest.main()