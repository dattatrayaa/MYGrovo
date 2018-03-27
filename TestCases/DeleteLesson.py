'''
Created on 13-Mar-2018

@author: Sheethu C
'''
import os
import time
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import driver


class DeleteLesson:
    def lessonDelete(self,lessonname):  
        try:                                                       
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
            print "Clicking on Lessons button from side menu"
            driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
            wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-table")))
            driver.find_element_by_id("search-lessons-in-table").send_keys(lessonname)
            driver.find_element_by_id("search-lessons-in-table").send_keys(Keys.ENTER)
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/button[2]")))  
            ele=driver.find_elements_by_xpath("//tbody/tr/td[2]/a[.='"+lessonname+"']/../../td[4]/button[.='Delete']")
            count=len(ele)
            print count
            for count in range (0,count):
                wait.until(EC.element_to_be_clickable((By.XPATH,"//tbody/tr[1]/td[2]/a[.='"+lessonname+"']/../../td[4]/button[.='Delete']")))
                driver.find_element_by_xpath("//tbody/tr[1]/td[2]/a[.='"+lessonname+"']/../../td[4]/button[.='Delete']").click()
                #driver.find_element_by_xpath("//tr[1]/td[4]/button[.='Delete']").click()
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[.='Delete']")))
                wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[.='Delete']")))
                delo = driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[.='Delete']")
                driver.execute_script('arguments[0].click()',delo)
                #print "Deleted"
                wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[1]/button")))
                driver.refresh()
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)

