'''
Created on 21-Feb-2018

@author: QA
'''

import time
import xlrd
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

class BaseTestClass:
    
    def userLogin(self):
    
        print "Opening Browser"
        driver.maximize_window()
        
        print "Reading Login Credentials from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        
        print ("Fetching Sheet Name\n")
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        print("Fetching the URL, username and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        url = cell.value
        print "Grovo URL is : %s." % url
        
        cell = first_sheet.cell(3,1)
        username = cell.value
        print "User Name is : %s." % username
        
        cell = first_sheet.cell(3,2)
        password = cell.value
        print "Password is : %s." % password
        
        print ("Redirecting to specified URL\n")
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        #hi
        element.send_keys(Keys.TAB)
        print ("Clicking on Sign_In button\n")
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged In to Grovo Application"
        time.sleep(5)
