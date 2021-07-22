from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from msedge.selenium_tools import Edge, EdgeOptions
from random import randint, randrange
import time
import random

URL = 'https://www.amazon.com/DP/B08WM28PVH'

WAIT_TIME = 5
PRICE_LIMIT = 700.00


class Shopping:
    def __init__(self, mail, password):
       
        self.mail = mail
        self.password = password
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument('-inprivate')
        self.driver = Edge(
            executable_path='msedgedriver.exe', options=options)

    
    def logIn(self):
       

        driver = self.driver  

        
        mail_elem = driver.find_element_by_xpath("//input[@name='email']")
        mail_elem.clear()
        mail_elem.send_keys(self.mail)

        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        mail_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

      
        password_elem = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        password_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

   
    def findProduct(self):
        
        driver = self.driver
        driver.get(URL)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

      
        isAvailable = self.productStatus()

        if isAvailable == 'See Similar Items':
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
        elif isAvailable <= PRICE_LIMIT:
        
            buy_now = driver.find_element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.logIn()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

	        # Deliver This Adress
	    
            deliver_noww = driver.find_element_by_class_name('a-declarative')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            deliver_noww.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

         
            place_order_text = driver.find_element_by_name(
                'placeYourOrder1').text
            place_order = driver.find_element_by_name('placeYourOrder1')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            print(f'***** ORDERED: {place_order_text}')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            place_order.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

        else:
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()

    def productStatus(self):
        
        driver = self.driver
        available = driver.find_element_by_class_name('a-button-text').text
        if available == 'See Similar Items':
            print(f'***** ESTADO - STATUS: {available}')
            return available
        else:
            print(f'***** PRECIO - PRICE: {available}')
            return float(available[6:])  

    def closeBrowser(self):
        """ Closes browser """
        self.driver.close()


if __name__ == '__main__':
    shopBot = Shopping(mail="yourmail@mail.com",
                       password="your_password")
    shopBot.findProduct()
    shopBot.closeBrowser()