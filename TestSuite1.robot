*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

#Fucntions for Test Bed cleanup
Library   TestCases/Delete_Tags_Attributes_Lessons.py

#Functions to create Lessons
Library   TestCases/BlankLessonOne.py
Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py
Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py

#Functions to create Tracks
Library   TestCases/TrackWithTxtImgQueLesson.py
Library   TestCases/TrackWithDocumentLesson.py
Library   TestCases/TrackWithImageLesson.py
Library   TestCases/TrackWithQuestionLesson.py

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

#functions for Create Campaign With TRACKS
Library           TestCases/CampaignCreateTrackWithTextLesson.py
Library           TestCases/CampaignCreateTrackWithImageLesson.py
Library           TestCases/CampaignCreateTrackWithVideoLesson.py
Library           TestCases/CampaignCreateTrackWithDocumentLesson.py
Library           TestCases/CampaignCreateTrackWithQuestionLesson.py

Library           TestCases/CampaignTrackAllCardsOnetimeLesson.py
Library           TestCases/CampaignTrackAllCardsTwoTimeLesson.py
Library           TestCases/CampaignTrackTxtImgQueLesson.py
Library           TestCases/CampaignTrackVidDocQueLesson.py
Library           TestCases/CampaignTrackTxtVidQueLesson.py
Library           TestCases/CampaignTrackTextLessonImageLesson.py
Library           TestCases/CampaignTrackImageLessonVideoLesson.py
Library           TestCases/CampaignTrackVideoDocumentQuestionsLessons.py
Library           TestCases/CampaignTrackQuesAllCardsOneAllCardsTwoTime.py
Library           TestCases/CampaignTrackFourLessonsOne.py
Library           TestCases/CampaignTrackFourLessonsTwo.py
Library           TestCases/CampaignTrackFourLessonsThree.py

Library           TestCases/DeleteLesson.py



*** Test Cases ***
TC0 - User Login
    User Login

CreateCampTrackTextLesson
    Campaign For Track With Text Lesson

CreateCampTrackImageLesson
    Campaign For Track With Image Lesson

CreateCampTrackVideo
    Campaign For Track With Video Lesson

CreateCampTrackDocLesson
    Campaign For Track With Document Lesson

CreateCampTrackQuesLesson
    Campaign For Track With Question Lesson

CampaignTrackAllCardsOnetimeLesson
    Campaign For Track With All Cards One Time

CampaignTrackAllCardsTwoTimeLesson
    Campaign For Track With All Cards Two Time

CampaignTrackTxtImgQueLesson
    Campaign For Track With Text Image Question Lesson

CampaignTrackVidDocQueLesson
    Campaign For Track With Video Document Question Lesson

CampaignTrackTxtVidQueLesson
    Campaign For Track With Text Video Question Lesson

CampaignTrackTextLessonImageLesson
    Campaign For Track With Text Lesson Image Lesson

CampaignTrackImageLessonVideoLesson
    Campaign For Track With Image Lesson Video Lesson

CampaignTrackVideoDocumentQuestionsLessons
    Campaign For Track With Video Lesson Document Lesson Question Lesson

CampaignTrackQuesAllCardsOneAllCardsTwoTime
    Campaign For Track With Question Lesson All Cards One All Cards Two Time

CampaignTrackFourLessonsOne
    Campaign For Track With Four Lessons One

CampaignTrackFourLessonsTwo
    Campaign For Track With Four Lessons Two

CampaignTrackFourLessonsThree
    Campaign For Track With Four Lessons Three

DeleteLesson
    Main Delete
