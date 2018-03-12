'''
Created on 22-Feb-2018

@author: dattatraya
'''
import os.path

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd


class LessonCreateDocument:
    def lessonWithDocument(self,lessonname,documentPath,timeToUploaddocument):
        print "This is lesson with document"
        
        wait=WebDriverWait(driver, timeToUploaddocument)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)

        
               
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        
        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one Text card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonname)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonname
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Document card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        
        
        
        #Uploading Document
        print "Uploading Document"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")))
        
        documentContainerlocator_afterupload= driver.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")
        
        if(documentContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Document file"
            raise Exception
        
        
        
        print "Publishing lesson"
        
        publishbutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        
        driver.execute_script("arguments[0].click();",publishbutton)

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
        
        '''# verifying success message
        
        
        
        print "Verifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        print "Message '"+headerText+"' is displayed"
        
        if "You have successfully published" in headerText:
            print("Create a new lesson tab is displayed")
        else:
            print "Success message is not displayed"
            raise Exception'''

        print "Lesson published"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        #Verifying created lesson is displayed in list
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonname
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()



    def lessonWithDocumentUploadCard(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(26,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(27,1)
        documentpath = cell2.value
        
        cell3 = first_sheet.cell(28,1)
        giveTimetoUploadDocument = cell3.value
        
        try:
            doc=LessonCreateDocument()
            doc.lessonWithDocument(lessonname, documentpath, giveTimetoUploadDocument)
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
        

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m3=LessonCreateDocument()
    m3.lessonWithDocumentUploadCard()
    