'''
Created on 07-Mar-2018

@author: dattatraya
'''

import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CreateTrackComman:
    
    
    
    def createTrack(self,titleOfTrack,Imagefilepath,description,tagName,lessonname,expectedSuccessText):
        
        try:
            print "Creating track with one lesson contains Text Card"
            
            wait=WebDriverWait(driver, 100)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
            
            print "Clicking on Lessons button from side menu"
            driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
            
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a")))
            print "Clicking on Track button from side menu"
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a").click()
            
            createTrackbutton=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
            
            createTrackbutton.click()
            
            print "Entering title"
            titlefield=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='title']")))
            titlefield.send_keys(titleOfTrack)
            print "Title entered ::"+titleOfTrack
            
            driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath)
            print "waiting to upload image"
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/img")))
            print "Image uploaded"
            
            print "Entering Description"
            driver.find_element_by_xpath(".//*[@id='description']").send_keys(description)
            print "Description entered ::"+description 
            
            
            
            print "Adding tag"
            addTags=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
            webdriver.ActionChains(driver).move_to_element(addTags).click().send_keys(tagName).perform()
            
            option=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='react-select-2--option-0']")))
            webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
            
            driver.find_element_by_xpath(".//*[@id='description']").send_keys(" ")
            
            
            print "Adding created lesson"
            
            print "Clicking on Add lessons button"
           
            driver.execute_script("window.scrollTo(0, 0);")
            addlessonbutton=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/button")
            addlessonbutton.click()
            
            
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]/div")))
            
            print "Searching for lesson in Add lessons pop up"
            driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonname)
            
            searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonname+"']/../../div[1]/div")))
            searchedLesson.click()
            
            print "Lesson '"+lessonname+"' selected"
            print "Adding to Track"
            driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
            
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div")))
            
            print "Checking added lesson is selected lesson from Pop up"
            lessonTextAddedToGrid=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div").text
    
            if lessonTextAddedToGrid==lessonname:
                print "Selected Lesson is displayed in grid of tracks page"
            
            else:
                print "Lesson is not displayed"
                raise Exception
            
            print "Clicking on Publish Track button"
            
            wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button").click()
            
            time.sleep(3)
            
            '''print "Verifying Success message is displaying"
            
            
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
            actualSuccessText=driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
            
            if actualSuccessText==expectedSuccessText:
                print "Success message '"+actualSuccessText+"' is displayed"
            else:
                print "failed to display expected success message"
                raise Exception'''
            
            
            print "Verifying Creates track '"+titleOfTrack+"' is displayed in Tracks grid"
            
            
          
            
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[1]/a").click()
            
            wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
            
            trackInGrid=driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']").text
            
            if trackInGrid==titleOfTrack:
                print "Track '"+trackInGrid+"' is displayed in grid"
            else:
                print "Track is not displayed in grid"
                raise Exception
            
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
            
            
        except Exception:
            try:
                WebDriverWait(driver, 20).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                
                print("no alert")
        
         
