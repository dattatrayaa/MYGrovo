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


class CampaignCreateTrackWithDocumentLesson:
    
    def campWithTrackDocumentlesson(self,campaignTitle,campDescription,trackName,actualSuccessMessage):
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
    
    
    
    
    
        
    def CampaignForTrackWithDocumentLesson(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(46,4)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(47,4)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(48,4)
        actualSuccessMessage = cell1.value
        
        #Track
        cell1 = first_sheet.cell(50,4)
        trackName = cell1.value
        
        cell2 = first_sheet.cell(51,4)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(52,4)
        description = cell2.value
        
        cell2 = first_sheet.cell(53,4)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(54,4)
        expectedSuccessText= cell2.value
        
        #Lesson
        cell2 = first_sheet.cell(56,4)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(57,4)
        documentPath= cell2.value
        
        cell2 = first_sheet.cell(58,4)
        timeToUploaddocument= cell2.value
      
        
       
        
        try:
            #lesson Creation
            obj=CreateLessonDifferentLessons()
            obj.lessonWithDocument(lessonName, documentPath, timeToUploaddocument)
            
            #Track Creation
            obj1=CreateTrackComman()
            obj1.createTrack(trackName, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            
            #Campaign Creation
            obj2=CampaignCreateTrackWithDocumentLesson()
            obj2.campWithTrackDocumentlesson(campaignTitle, campDescription, trackName, actualSuccessMessage)
        
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
    
    
 