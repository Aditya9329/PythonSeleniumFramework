from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pytest
from selenium.webdriver.support.select import Select
import time

"""
imlllllllliclllllllt wait is a kind of a globa ltimeout 
if 5 sec is set max but object appear before that i will  proceed further.
"""

from selenium.webdriver import ActionChains
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_endToend(self):
        
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getProducts()
        

        for product in products:
            productName = product.find_element(By.XPATH,"div/h4/a").text
            if productName == 'Blackberry':
                product.find_element(By.XPATH,"div/button").click()

        checkOutPage.getCheckOutAfterAddToCart().click()

        checkOutPage.getFinalCheckOut().click()

        confirmPage = ConfirmPage(self.driver)

        confirmPage.getCountry().send_keys("ind")

        wait = WebDriverWait(self.driver,10)

        wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))

        confirmPage.getDeliverLocation().click()

        confirmPage.getAgreeTerms().click()
        
        confirmPage.getPurchaseBtn().click()