'''
Created on 07-Mar-2018

@author: dattatraya
'''
import os.path
import traceback

from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman


class CampaignCreateTrackWithTextLesson:
    
    
    def campWithTrackTextlesson(self,campaignTitle,campDescription,trackName,actualSuccessMessage):
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
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        #verifying success message
        print "\nVerifying success message"
        
        if elements.successMessage()==actualSuccessMessage:
            print "Message '"+actualSuccessMessage+"' is displayed"
        else:
            print "Success message is not displayed properly"
            raise Exception
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
    
    
    
    
    
        
    def CampaignForTrackWithTextLesson(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(1,7)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(2,7)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(3,7)
        actualSuccessMessage = cell1.value
        
        #Track
        cell1 = first_sheet.cell(5,7)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(6,7)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(7,7)
        description = cell2.value
        
        cell2 = first_sheet.cell(8,7)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(9,7)
        expectedSuccessText= cell2.value
        
        #Lesson
        cell2 = first_sheet.cell(11,7)
        lessonname= cell2.value
        
        cell2 = first_sheet.cell(12,7)
        textCard= cell2.value
      
        
       
        
        try:
            #lesson Creation
            obj=CreateLessonDifferentLessons()
            obj.lessonWithText(lessonname, textCard)
            
            #Track Creation
            obj1=CreateTrackComman()
            obj1.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            
            
            #Campaign Creation
            obj2=CampaignCreateTrackWithTextLesson()
            obj2.campWithTrackTextlesson(campaignTitle, campDescription, titleOfTrack, actualSuccessMessage)
         
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
        finally: 
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
    
    
 