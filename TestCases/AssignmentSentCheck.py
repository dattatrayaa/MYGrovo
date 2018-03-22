'''
Created on 15-Mar-2018

@author: dattatraya
'''

import time

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class AssignmentSentCheck:
    
    
    #EmployeeId,Password,campaignTitle,lessonName
    
    def assignmentCheck(self,EmailId,Password,campaignTitle,lessonName,username,password):
        
        print "\n\nChecking sent assignment is displayed for User"
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        
        
        print "Logging out"
        print "Clicking on Username Dropdown"
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
        print "Clicked on Sign Out option"
        
        element = wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(EmailId)
       
        print "Entering Password"
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Users account"
        time.sleep(4)
        
        
        assignmentText=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/a[1]/span")))
        
        if campaignTitle in assignmentText.text:
            print "Campaign displayed for User in Current assignment section"
            
        else:
            print "Campaign not displayed for User"
            raise Exception
        
        print "Starting assignment"
        
        
        startButton=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/a[2]")))
        startButton.click()
        
        print "Waiting for lesson name to be displayed"
        
        lessonNameForUser=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div[1]/h1/span")))
        lessonNameForUserText=lessonNameForUser.text
        if lessonName==lessonNameForUserText:
            print "Verified Lesson '"+lessonNameForUserText+"' is displayed for User"
        else:
            print "Lesson displayed is not valid"
            raise Exception
        
        
        backButtoon=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[1]/span/button")))
        backButtoon.click()
        
        unDropDown=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        driver.execute_script('arguments[0].click()',unDropDown)
        
        signOut=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',signOut)
        
        
        
        element = wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Users account"
        
        time.sleep(5)
        
        
        
        
    '''def assignmentCheck(self,EmailId,Password,campaignTitle,username,password,lessonName1, lessonName2, lessonName3, lessonName4):
        
        print "\n\nChecking sent assignment is displayed for User"
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        
        
        print "Logging out"
        print "Clicking on Username Dropdown"
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
        print "Clicked on Sign Out option"
        
        element = wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(EmailId)
       
        print "Entering Password"
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Users account"
        time.sleep(4)
        
        
        assignmentText=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/a[1]/span")))
        
        if campaignTitle in assignmentText.text:
            print "Campaign displayed for User in Current assignment section"
            
        else:
            print "Campaign not displayed for User"
            raise Exception
        
        print "Starting assignment"
        
        
        startButton=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/a[2]")))
        startButton.click()
        
        print "Waiting for lesson name to be displayed"
        
        lessonNameForUser=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div[1]/h1/span")))
        lessonNameForUserText=lessonNameForUser.text                   
        if lessonName1==lessonNameForUserText:
            print "Verified Lesson '"+lessonNameForUserText+"' is displayed for User"
        else:
            print "Lesson displayed is not valid"
            raise Exception
        
        print "\nPlaying Lesson"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div/div/div")))
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[5]/div/span/button").click()
        
        complete=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[1]/div/h1")))
        
        if complete.text=="COMPLETE":
            print "Lesson completed"
        else:
            print "Complete text is not showing"
            raise Exception
        
        
        
        
        
        #second
        print "Clicking on Next Lesson"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/a/div[1]/div/span").click()
        
        lessonNameForUser1=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div[1]/h1/span")))
        lessonNameForUserText1=lessonNameForUser1.text                   
        if lessonName2==lessonNameForUserText1:
            print "Verified Lesson '"+lessonNameForUserText1+"' is displayed for User"
        else:
            print "Lesson displayed is not valid"
            raise Exception
        
        print "\nPlaying Lesson"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[5]/div/span/button").click()
        
        complete=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[1]/div/h1")))
        
        if complete.text=="COMPLETE":
            print "Lesson completed"
        else:
            print "Complete text is not showing"
            raise Exception
        
        
        
        
        
        
        ##Third lesson
        print "Clicking on Next Lesson"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/a/div[1]/div/span").click()
        
        lessonNameForUser2=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div[1]/h1/span")))
        lessonNameForUserText2=lessonNameForUser2.text                   
        if lessonName3==lessonNameForUserText2:
            print "Verified Lesson '"+lessonNameForUserText2+"' is displayed for User"
        else:
            print "Lesson displayed is not valid"
            raise Exception
        
        
        print "\nPlaying Lesson"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[5]/div/span/button").click()
        
        complete=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[1]/div/h1")))
        
        if complete.text=="COMPLETE":
            print "Lesson completed"
        else:
            print "Complete text is not showing"
            raise Exception
        
        
        
        
        #Fourth
        print "Clicking on Next Lesson"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[5]/div/span/button").click()
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/a/div[1]/div/span").click()
        
        lessonNameForUser3=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div[1]/h1/span")))
        lessonNameForUserText3=lessonNameForUser3.text                   
        if lessonName4==lessonNameForUserText3:
            print "Verified Lesson '"+lessonNameForUserText3+"' is displayed for User"
        else:
            print "Lesson displayed is not valid"
            raise Exception
        
        print "\nPlaying Lesson"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[4]/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div/div/div")))
        
        ans1=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/div/div")))
        
        ans1.click()
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[5]/div/span/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[5]/div/span/button").click()
        
        complete=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div/div[4]/div/div/div/div/div[1]/h1")))
        
        if complete.text=="ASSIGNMENT\nCOMPLETE":
            print "Assignment completed"
        else:
            print "Complete text is not showing"
            raise Exception
        
        
        
        
        
        backButtoon=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div/div[1]/span/button")))
        backButtoon.click()
        
        unDropDown=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        driver.execute_script('arguments[0].click()',unDropDown)
        
        signOut=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',signOut)
        
        
        
        element = wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Users account"
        
        time.sleep(5)'''
        
        
        
        
        
        
        
        
'''if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    hk=AssignmentSentCheck()
    hk.assignmentCheck("email_2010_@gmail.com", "Data@123", "CampForAssignOneTrackOneLesson", "Lesson_for_Assignment_Learner_1LessonTrack", "mymaster@gmail.com", "Data@123")
        
        
        '''
        
        
        

