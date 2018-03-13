*** Settings ***

#Config
Library   TestCases/BaseTestClass.py




#Functions to create Campaign
Library   TestCases/CreateCampaignForTextLesson.py
Library   TestCases/CreateCampaignForImageLesson.py
Library   TestCases/CreateCampaignForVideoLesson.py
Library   TestCases/CreateCampaignForDocumentLesson.py
Library   TestCases/CreateCampaignForQuestionLesson.py
Library   TestCases/CreateCampaignForAllCardsOneTime.py
Library   TestCases/CreateCampaignForTxtImgQueLesson.py
Library   TestCases/CreateCampaignForAllCardsTwoTime.py
Library   TestCases/CreateCampaignForTxtVidQuesLesson.py
Library   TestCases/CreateCampaignForVidDocQueLesson.py
Library   TestCases/CreateCampaignForFourLessonsOne.py
Library   TestCases/CreateCampaignForFourLessonsTwo.py
Library   TestCases/CreateCampaignForFourLessonsThree.py
Library   TestCases/CreateCampaignForTextAndImageLesson.py
Library   TestCases/CreateCampaignForImageAndVideoLesson.py
Library   TestCases/CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons.py
Library   TestCases/CreateCampaignForVideoLsnDocLsQuestionLes.py
Library   TestCases/CampaignPageDisplay.py

#Functions for User Creation with standard roles
Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py

Library           TestCases/DeleteLesson.py


*** Test Cases ***
TC1
    User Login

CreateCampaignForTextLesson
    Create Campaign Text Lesson

CreateCampaignForImageLesson
    Create Campaign Image Lesson

CreateCampaignForVideoLesson
    Create Campaign Video Lesson

CreateCampaignForDocumentLesson
    Create Campaign Document Lesson

CreateCampaignForQuestionLesson
    Create Campaign Question Lesson


CreateCampaignForAllCardsOneTime
    Create Campaign All Cards One Time Lesson

CreateCampaignForAllCardsTwoTime
    Create Campaign With All Cards Two Time Lesson
	
CreateCampaignForTxtImgQueLesson
    Create Campaign Text Image Ques Lesson

CreateCampaignForTxtVidQuesLesson
    Create Campaign With Lesson Text Video Question

CreateCampaignForVidDocQueLesson
    Create Campaign With Lesson Video Document Question

CreateCampaignForTextAndImageLesson
    Create Campaign With Text Lesson Image Lesson

CreateCampaignForImageAndVideoLesson
    Create Campaign With Image Lesson Video Lesson

CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons
    Create Campaign With Three Lessons

CreateCampaignForVideoLsnDocLsQuestionLes
    Create Campaign With Video Lesson Document Lesson Question Lesson
	

CreateCampaignForFourLessonsOne
    Create Campaign With Four Lessons One

CreateCampaignForFourLessonsTwo
    Create Campaign With Four Lessons Two

CreateCampaignForFourLessonsThree
    Create Campaign With Four Lessons Three


DeleteLesson
    Main Delete
