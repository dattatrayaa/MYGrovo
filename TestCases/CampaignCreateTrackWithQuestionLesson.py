'''
Created on 07-Mar-2018

@author: dattatraya
'''

import os.path
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman


class CampaignCreateTrackWithQuestionLesson:
    
    def campWithTrackQuestionlesson(self,campaignTitle,campDescription,trackName,actualSuccessMessage,minPassingScore,numberOfAttempts,ownDuration):
        elements=CampPage()
        
        wait=WebDriverWait(driver, 60)
        
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
        print "Adding Track"
        #Add Track 
        
        elements.addTrackButton()
        
        #Searching track and adding
        elements.searchTracksAndSelect(trackName)
        
        #Adding to Campaign
        elements.addToCampaignTrack()
        
        
        #Verifying Added Track is displayed in Grid
        print "\nVerifying Added Track is displayed in Grid"
        if trackName in elements.firstTrackInGrid():
            print "Track displayed in grid"
        else:
            print "Track not displayed in grid"
            
            
        #Making as Graded campaign
        print "Making this as a graded campaign"
        elements.setOwnDuration(ownDuration)
        
        elements.makeThisAsAGradedCampaign()
        
        elements.setMinimumPassingScore(minPassingScore)    
        
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        '''#verifying success message
        print "\nVerifying success message"
        
        if elements.successMessage()==actualSuccessMessage:
            print "Message '"+actualSuccessMessage+"' is displayed"
        else:
            print "Success message is not displayed properly"
            raise Exception'''
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        #verifying in Campaigns displayed in Campaigns grid
        elements.searchingForlesson(campaignTitle)
        
        if elements.actualCampTitleINGrid()==campaignTitle:
            print "Campaign '"+campaignTitle+"' displayed in Grid"
        
        else:
            print "Campaign is not displayed in Grid"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
    
    
    
    
    
        
    def CampaignForTrackWithQuestionLesson(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(62,4)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(63,4)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(64,4)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(65,4)
        minPassingScore = cell1.value
        
        cell1 = first_sheet.cell(66,4)
        numberOfAttempts = cell1.value
        
        cell1 = first_sheet.cell(67,4)
        ownDuration = cell1.value
        
        #Track
        cell1 = first_sheet.cell(69,4)
        trackName = cell1.value
        
        cell2 = first_sheet.cell(70,4)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(71,4)
        description = cell2.value
        
        cell2 = first_sheet.cell(72,4)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(73,4)
        expectedSuccessText= cell2.value
        
        #Lesson
        cell2 = first_sheet.cell(75,4)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(76,4)
        questionCard= cell2.value
        
        cell2 = first_sheet.cell(77,4)
        ans1= cell2.value
        
        cell2 = first_sheet.cell(78,4)
        ans2= cell2.value
      
        
       
        
        try:
            #lesson Creation
            obj=CreateLessonDifferentLessons()
            obj.lessonWithQuestion(lessonName, questionCard, ans1, ans2)
            
            #Track Creation
            obj1=CreateTrackComman()
            obj1.createTrack(trackName, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            
            #Campaign Creation
            obj2=CampaignCreateTrackWithQuestionLesson()
            obj2.campWithTrackQuestionlesson(campaignTitle, campDescription, trackName, actualSuccessMessage, minPassingScore, numberOfAttempts, ownDuration)
         
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
        finally:  
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
    
    
    
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    ol=CampaignCreateTrackWithQuestionLesson()
    ol.CampaignForTrackWithQuestionLesson()
    
    


    