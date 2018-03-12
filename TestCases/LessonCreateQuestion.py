'''
Created on 22-Feb-2018

@author: dattatraya
'''
import os.path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver


class LessonCreateQuestion():
    
    
    def createLesson(self,lessonName,questionCard,ans1,ans2,ans3):
        wait=WebDriverWait(driver, 60)
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
        
        print "Creating New lesson With one question card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        
        print "Entered lesson name ::"+lessonName
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
        questionArea=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        questionArea.send_keys(questionCard)
        print "Question entered ::"
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "First Answer entered "
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
        print "First Answer entered "
        
        print "Selecting 'Add a answer choice"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div").click()
        ansC=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-2']")))
        
        print "\nVerifying Answer choice 'C' is displaying"
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-2']").is_displayed():
            print "Verified Answer choice C is displayed"
        else:
            print "Answer choice c is not displayed"
            raise Exception
        
        print "Entering Third answer choice"
        ansC.send_keys(ans3)
        print "Third Answer entered "

         
        
        print "\nVerifying All the data entered is displaying in fields"
        
        if questionArea.text==questionCard:
            print "Question ::"+questionCard
        else:
            print "Question is not displayed"
            raise Exception
        
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").text==ans1:
            print "Answer 1 ::"+ans1
        else:
            print "Answer 1 is not displayed"
            raise Exception
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").text==ans2:
            print "Answer 2 ::"+ans2
        else:
            print "Answer 2 is not displayed"
            raise Exception
        
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-2']").text==ans3:
            print "Answer 3 ::"+ans2
        else:
            print "Answer 3 is not displayed"
            raise Exception
        
        
        #Verifying Correct answer displayed
        print "\nVerifying by default correct answer selected as A"
        
        if driver.find_element_by_xpath("//input[@id='question-answer-correct-0']").is_selected():
            print "Verified Radio button for Correct answer A is selected"
        else:
            print "Radio button is not selected"
            raise Exception
        
        
        
        publishbutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        
        driver.execute_script("arguments[0].click();",publishbutton)

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        '''print "\nVerifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        
        
        if "You have successfully published" in headerText:
            print "Message '"+headerText+"' is displayed"
        else:
            print "Success message is not displayed"
            raise Exception
'''
        print "Lesson published"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        
        print "\nVerifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
       
    def lessonWithQuestionAnswerCard(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        cell1 = first_sheet.cell(6,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(7,1)
        question = cell2.value
        
        cell3 = first_sheet.cell(8,1)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(9,1)
        ans2 = cell4.value
        
        cell5 = first_sheet.cell(10,1)
        ans3 = cell5.value
        
        try:
            que=LessonCreateQuestion()
            que.createLesson(lessonname, question,ans1,ans2,ans3)
          
        finally:    
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
    

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m1=LessonCreateQuestion()
    m1.lessonWithQuestionAnswerCard()