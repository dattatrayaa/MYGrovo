from operator import contains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseTestClass import driver

import os.path
import xlrd
import time
class CreateLearner():
    
    def creatLearnereuser(self):
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateuserfromUI')
        print("Fetching the First Name, LastName,Email,EmployeeId and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        FirstName = cell.value
        print FirstName
        
        cell = first_sheet.cell(1,2)
        LastName = cell.value
        print LastName
        
        cell = first_sheet.cell(1,3)
        Email = cell.value
        print Email
        
        cell = first_sheet.cell(1,4)
        EmployeeId = cell.value
        print EmployeeId
        
        cell = first_sheet.cell(1,6)
        Password = cell.value
        print Password
        
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
        driver.find_element_by_xpath("//button[.='Save']").click()
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
    
    
    def createLearnerLogin(self):
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateuserfromUI')
        print("Fetching the First Name, LastName,Email,EmployeeId and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,3)
        Email = cell.value
        print Email
        
        cell = first_sheet.cell(1,6)
        Password = cell.value
        print Password
        
        cell = first_sheet.cell(1,7)
        NewPassword = cell.value
        print NewPassword
        
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
        wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
        print "Home Page is Loaded"
        
        print "Learner Home Page Verification"
        expectedresult = "Home"
        expectedresult1="Library"
        actualresult = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[1]/a[2]/span").text
        actualresult1 = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[1]/a[3]/span").text
        if(expectedresult == actualresult):
            if(expectedresult1==actualresult1):
                print"User is able to login and Dashboard is displayed.."
        else:
            print"User not able to login.."
            raise Exception    
        print "Sign out "
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
    def againuserLogin(self):
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        
        # print number of sheets
        print("Number of WorkSheets :")
        print book.nsheets
    
        # print sheet names
        #print("Name of WorkSheets :")
        #print book.sheet_names()
        
        # get the first worksheet
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        # read a row
        #print("First Row Data in 1st WorkSheet :")
        #print first_sheet.row_values(0)
        
        print("Fetching the URL, username and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        url = cell.value
        print url
        
        cell = first_sheet.cell(3,1)
        username = cell.value
        print username
        
        cell = first_sheet.cell(3,2)
        password = cell.value
        print password  
        
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
           
        
    def createLearnerUserAndValidation(self):
     
        try :
           ob =CreateLearner()
           ob.creatLearnereuser()
           ob.createLearnerLogin() 
           ob.againuserLogin() 
           
        finally:  
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            
            print "Home Page Loaded"
            
