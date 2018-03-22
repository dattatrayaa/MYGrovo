'''
Created on 27-Feb-2018

@author: dattatraya
'''

import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CampPage:
    
    def campaignButtonFromSideMenuXpath(self):
        time.sleep(2)
        return "(//a[@href='/plan/campaigns'])[1]"
    
    
    def createCampaignButtonXpath(self):
        time.sleep(2)
        return "//a[@href='/plan/campaigns/new/edit']"
    
    def Camp_titleXpath(self):
        time.sleep(2)
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
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li[1]/div[2]/div/h4/div/span")))
        return driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div/span").text
    
    def secondLessonInGrid(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li[2]/div[2]/div/h4/div/span")))
        return driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div/span").text
        
    def thirdLessonInGrid(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li[3]/div[2]/div/h4/div/span")))
        return driver.find_element_by_xpath("//li[3]/div[2]/div/h4/div/span").text
        
    def fourthLessonInGrid(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li[4]/div[2]/div/h4/div/span")))
        return driver.find_element_by_xpath("//li[4]/div[2]/div/h4/div/span").text
        
        
    def successMessage(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
        return driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
        
        
    def saveAndExitButton(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/button[2]")))
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
        
        wait=WebDriverWait(driver, 150)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//ul/li[1]/div[1]")))
        driver.find_element_by_xpath(".//*[@id='search-objectives-in-modal']").send_keys(trackName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//li/div[2]/h4[.='"+trackName+"']/../../div[1]/div)[1]")))
        
        driver.find_element_by_xpath("(//li/div[2]/h4[.='"+trackName+"']/../../div[1]/div)[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='search-objectives-in-modal']").clear()
        
        
    def addToCampaignTrack(self):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[contains(.,'campaign')]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[contains(.,'campaign')]").click()
        
    
    def firstTrackInGrid(self):
        return driver.find_element_by_xpath("(//li/div/span[2]/em)[1]").text
    
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
        
        
        
    def saveAndPlanAssignmentbutton(self):
        wait=WebDriverWait(driver, 60)
        savePlan=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/button[1]")))
        savePlan.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='campaign-due-date']")))
        
        
        
    def planAssignementForHeaderText(self):
        return driver.find_element_by_xpath("//header/h1[contains(.,'Plan')]").text
        
    def assignDateValue(self):
        time.sleep(2)
        return driver.find_element_by_xpath("//input[@name='campaign-assign-date']").get_attribute("value")  
        
    def dueDateValue(self):
        
        return driver.find_element_by_xpath("//input[@name='campaign-due-date']").get_attribute("value")
    
    def addingUser(self,nameOFuser):
        wait=WebDriverWait(driver, 60)
        
        ele=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
        print "Searching for user"
        webdriver.ActionChains(driver).move_to_element(ele).click().send_keys(nameOFuser).perform()
        
        option=wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@role='option'])[1]")))
        webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
        print "User added"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/section[2]/div/table/tbody/tr/td[1]")))
        
        
    def userInGrid(self):
        return driver.find_element_by_xpath("(//table/tbody/tr/td[1])[1]").text
        
        
    def sendAssignment(self):
        wait=WebDriverWait(driver, 60)
        sendassign=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/section[2]/div/div[4]/button")))
        sendassign.click()
        
        
    def confirmPopupsendingAssignement(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[1]/h3")))
        return driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/h3")
        
        
    def sendAssignmentFromPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div[1]/h1/em")))
    
        
        
        
        
        
        
        
        
        
        
        