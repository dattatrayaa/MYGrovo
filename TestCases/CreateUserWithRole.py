'''
Created on 21-Mar-2018

@author: dattatraya
'''
import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from xlrd import open_workbook
import xlrd


class CreateUserWithRole:
    
    def create(self,FirstName,LastName,Email,EmployeeId,Password,role):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
        print "Clicked on Admin"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]").click()
        print "clicked on Users"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/div").click()
        print "Clicked on Add or editUser"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div").click()
        print "Clicked on Add An individual User"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header")))
        
        print "Verifying Add user Page"
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header").is_displayed():
            print("Add user Page is displayed")
        else:
            print ""
            raise Exception
        print "Verifying First Name field"
        wait.until(EC.visibility_of_element_located((By.ID,"create-edit-user-search-firstName")))
        if driver.find_element_by_id("create-edit-user-search-firstName").is_displayed():
            print(" First Name field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id("create-edit-user-search-firstName").send_keys(FirstName)
        print "FirstName is Entered ::"+FirstName
        print "Last NAme verifying"
        if driver.find_element_by_id("create-edit-user-search-lastName").is_displayed():
            print(" Last Name field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id("create-edit-user-search-lastName").send_keys(LastName)
        print "Last Name is Entered ::"+LastName
        print "Email verifying"
        if driver.find_element_by_id("create-edit-user-search-username").is_displayed():
            print("Email field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id("create-edit-user-search-username").send_keys(Email)
        print "Email is Entered ::"+Email
        
        print "Employee ID verifying"
        if driver.find_element_by_id("create-edit-user-search-employeeId").is_displayed():
            print("Employee ID field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id("create-edit-user-search-employeeId").send_keys(EmployeeId)
        print "Employee ID  is Entered ::"+EmployeeId
        
        
        
        
        
        print "Entering role into Direct Roles"
        directRoles=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
        
        webdriver.ActionChains(driver).move_to_element(directRoles).click().send_keys(role).perform()
        roledisplayed=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option' and contains (.,'"+role+"')]")))
        
        webdriver.ActionChains(driver).move_to_element(roledisplayed).click().perform()
        
        print "Role is selected"
        
        
        
        
        
        print "Inherited Role Verifying"
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[6]/div").is_displayed():
            print("Inherited Role field displayed")
        else:
            print ""
            raise Exception
        
        print "Password Field is Verifying"
        if driver.find_element_by_id("create-edit-user-search-new-password").is_displayed():
            print("Password field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id("create-edit-user-search-new-password").send_keys(Password)
        print "Password is Entered ::"+Password
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='Add']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.='Add']")))
        driver.find_element_by_xpath("//button[.='Add']").click()
        print "Clicked on add button"
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='Save']")))
        saveButton=driver.find_element_by_xpath("//button[.='Save']");
        driver.execute_script("arguments[0].click();",saveButton)
        
        
        print "Clicked on Save"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        driver.find_element_by_id("search-users").send_keys(FirstName)
        print "Searching for the Created User"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr[1]")))
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr/td[1]").text
        if(ele==FirstName):
            print("Created User Verified")
        else:
            print ""
            raise Exception  
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[2]/a/span[3]").click()
        print "Clicked on Account"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[2]/div[2]/a").click()
        print "Clicked on signOut Button"
        wait.until(EC.visibility_of_element_located((By.ID,"username")))
    
    
    def createLearnerLogin(self,Email,Password,NewPassword):
        
    
        wait=WebDriverWait(driver, 60)
        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(Email)
       
        print "Entering Password"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        wait.until(EC.visibility_of_element_located((By.ID,"currentPassword")))
        driver.find_element_by_id("currentPassword").send_keys(Password)
        print "Current Password is entered :"+Password
        driver.find_element_by_id("newPassword").send_keys(NewPassword)
        print "New Password is entered :"+NewPassword
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[1]/div[2]/button")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[1]/div[2]/button").click()
        
        
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[1]/div[2]/button")))
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='global-header-search']")))
        print "Home Page is Loaded"
        
        print "Learner Home Page Verification"
        actualresult = driver.find_element_by_xpath("(//a[@href='/plan/campaigns'])[1]")
        if actualresult.is_displayed():
            print"User is able to login and Dashboard is displayed.."
        else:
            print"User not able to login.."
            raise Exception    
        print "Sign out "
        
        
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
    
    


    def againLoginUser(self,url,username,password):
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
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Loged Into Grovo Application"
        time.sleep(5)


    def createUserWithRoleMain(self ,FirstName,LastName,Email,EmployeeId,Password,role,NewPassword,url, username, password):
        
        try:
            ob=CreateUserWithRole()
            ob.create(FirstName, LastName, Email, EmployeeId, Password, role)
            ob.createLearnerLogin(Email, Password, NewPassword)
            ob.againLoginUser(url, username, password)
        
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
        finally: 
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            #if any alert box occurs it will accept the alert
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
    