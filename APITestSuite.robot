*** Settings ***
Library   TestCases/BaseTestClass.py
Library   TestCases/BasicInformationValidData_27.py
Library   TestCases/BasicInformationWithDirectRole_28.py

*** Test Cases ***
TC0 - User Login
      User Login
 
TC1 - BasicInformationValidData_27 
      Basic Information Valid Data
    
TC2 - BasicInformationWithDirectRole_28
      Basic Information With Direct Role 


