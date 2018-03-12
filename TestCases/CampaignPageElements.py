'''
Created on 27-Feb-2018

@author: dattatraya
'''

import time

from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CampPage:
    
    def campaignButtonFromSideMenuXpath(self):
        return "(//a[@href='/plan/campaigns'])[1]"
    
    
    def createCampaignButtonXpath(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/header/div/div/a"
    
    def Camp_titleXpath(self):
        return ".//*[@id='campaign-title']"
        
    
    def Camp_DescriptionXpath(self):
        return ".//*[@id='campaign-description']"
    
    def Camp_AddLessonButtonXpath(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/section[2]/div[1]/div/button[1]"
        
    
    def FirstLessonWaitXpath(self):
        return "//li[1]/div[1]/div"
    
    def AddToCampaign_ButtonXpath(self):
        return "html/body/div[2]/div/div/div[2]/div[3]/button[1]"
    
    def SaveAndExit_ButtonXpath(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/button[2]"
    
    def titleTextField(self,campTitle):
        driver.find_element_by_xpath(".//*[@id='campaign-title']").send_keys(campTitle)
    
    def descriptionField(self,campDescription):
        driver.find_element_by_xpath(".//*[@id='campaign-description']").send_keys(campDescription)
    
    def addToCampaignButton(self):
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        
    def waitUntilSearchedLessonDisplayed(self,lessonName):
        wait=WebDriverWait(driver, 150)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonName+"']/../../div[1]/div")))
        
    def selectSearchedLesson(self,lessonName):
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonName+"']/../../div[1]/div").click()
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").clear()
        
    def searchLesson(self,lessonName):
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonName)
    
    def campaignsPageHeaderText(self):
        return driver.find_element_by_xpath("//header[@class='page-header']/h1").text
    
    def campaignButtonFromSideMenu(self):
        driver.find_element_by_xpath("(//a[@href='/plan/campaigns'])[1]").click()
    
    def addlessonButton(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/section[2]/div[1]/div/button[1]").click()
    
    def createCampaignButton(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/div/a").click()
        
        
    def firstLessonInGrid(self):
        return driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div/span").text
    
    def secondLessonInGrid(self):
        return driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div/span").text
        
    def thirdLessonInGrid(self):
        return driver.find_element_by_xpath("//li[3]/div[2]/div/h4/div/span").text
        
    def fourthLessonInGrid(self):
        return driver.find_element_by_xpath("//li[4]/div[2]/div/h4/div/span").text
        
        
    def successMessage(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
        return driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
        
        
    def saveAndExitButton(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div[2]/button[2]").click()
        
    def campaignDetailPageHeaderText(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div[1]/h1/em")))
        return driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div[1]/h1/em").text
    
    def makeThisAsAGradedCampaign(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/section[4]/div/div/label/span[2]").click()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='min-passing-score']")))
        
    def setMinimumPassingScore(self,minPassingScore):
        driver.find_element_by_xpath(".//*[@id='min-passing-score']").clear()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='min-passing-score']").send_keys(str(minPassingScore))
    
    def setAMaxNoOfAttempts(self,numberOfAttempts):
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/section[4]/div/div[2]/div[2]/div[2]/label/span[2]").click()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='input-campaign-attempts']")))
        
        driver.find_element_by_xpath(".//*[@id='input-campaign-attempts']").clear()
        driver.find_element_by_xpath(".//*[@id='input-campaign-attempts']").send_keys(str(numberOfAttempts))
        
        
    def addTrackButton(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/section[2]/div[1]/div/button[2]").click()
    
    
    def searchTracksAndSelect(self,trackName):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li[1]/div[1]")))
        driver.find_element_by_xpath(".//*[@id='search-objectives-in-modal']").send_keys(trackName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//li/div[2]/h4[.='"+trackName+"']/../../div[1]/div)[1]")))
        
        driver.find_element_by_xpath("(//li/div[2]/h4[.='"+trackName+"']/../../div[1]/div)[1]").click()
        
    def addToCampaignTrack(self):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        
    
    def firstTrackInGrid(self):
        return driver.find_element_by_xpath("//li[1]/div/span[2]/em").text
    
    def setOwnDuration(self,ownDuration):
        wait=WebDriverWait(driver, 60)
        days=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='input-campaign-duration']")))
    
        days.send_keys(str(ownDuration))
       
       
    def searchingForlesson(self,campName):
        wait=WebDriverWait(driver, 60)
        campButton=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[1]/a")))
         
        campButton.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='search-campaigns-in-table']")))
        driver.find_element_by_xpath(".//*[@id='search-campaigns-in-table']").send_keys(campName)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[1]/a[.='"+campName+"'])[1]")))
        
    def actualCampTitleINGrid(self):
        return driver.find_element_by_xpath("(//tbody/tr/td[1]/a)[1]").text
        
        
        
        
        
        
        
        
        
        
        
        
        
        