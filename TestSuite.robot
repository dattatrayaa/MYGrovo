*** Settings ***
Library   TestCases/BaseTestClass.py


Library   TestCases/BlankLessonFive.py
Library   TestCases/BlankLessonFiveTwo.py
Library   TestCases/BlankLessonOne.py
Library   TestCases/BlankLessonTen.py
Library   TestCases/BlankLessonTwo.py
Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py


Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py
Library   TestCases/CreateTagDocLesson.py
Library   TestCases/CreateTagImageLesson.py
Library   TestCases/CreateTagLessonCombinedLesson.py
Library   TestCases/CreateTagLessonExplainAconcept.py
Library   TestCases/CreateTagLessonIntroduceAtopic.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_1.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_2.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_3.py
Library   TestCases/CreateTagLessonMultiplecardlesson.py
Library   TestCases/CreateTagLessonPowerpoint.py
Library   TestCases/CreateTagLessonScorm.py
Library   TestCases/CreateTagLessonTeachAskill.py
Library   TestCases/CreateTagLessonTextLesson.py
Library   TestCases/CreateTagQuesLesson.py
Library   TestCases/CreateTagTrackLessonDocument.py
Library   TestCases/CreateTagTrackLessonFiveVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonImage.py
Library   TestCases/CreateTagTrackLessonOneTextImageVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonQuestion.py
Library   TestCases/CreateTagTrackLessonTenTextVideoQuestion.py
Library   TestCases/CreateTagTrackLessonTwoTextImageVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonVideo.py
Library   TestCases/CreateTagTrackWithTwolessons_1_2.py
Library   TestCases/CreateTagTrackWithTwolessons_2_3.py
Library   TestCases/CreateTagTrackWithfourlessons10_12_3.py
Library   TestCases/CreateTagTrackWithfourlessons4_5_6_7.py
Library   TestCases/CreateTagTrackWithfourlessons78910.py
Library   TestCases/CreateTagTrackWithonelesson_9.py
Library   TestCases/CreateTagTrackWiththreelessons_3_4_5.py
Library   TestCases/CreateTagTrackWiththreelessons_5_6_7.py
Library   TestCases/CreateTagTracklessonFiveTextImageQuestion.py
Library   TestCases/CreateTagVideoLesson.py
Library   TestCases/UserAttributeCheckboxWithReq.py
Library   TestCases/UserAttributeWithoutCheckbox.py
Library   TestCases/UserAttributeDateWithReq.py
Library   TestCases/UserAttributeDateWithoutReq.py
Library   TestCases/UserAttributeListWithReq.py
Library   TestCases/UserAttributeListWithoutReq.py
Library   TestCases/UserAttributeNumWithReq.py
Library   TestCases/UserAttributeNumWithoutReq.py
Library   TestCases/UserAttributeTextWithReq.py
Library   TestCases/UserAttributeTextWithoutReq.py
Library   TestCases/UserAttributeUserReferenceWithReq.py
Library   TestCases/UserAttributeUserReferenceWithoutReq.py
Library   TestCases/UserAttributeWithEmail.py
Library   TestCases/UserAttributeWithoutEmail.py



Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py
Library   TestCases/TrackWithDocumentLesson.py
Library   TestCases/TrackWithImageLesson.py
Library   TestCases/TrackWithQuestionLesson.py
Library   TestCases/TrackWithTextLesson.py
Library   TestCases/TrackWithTxtImgQueLesson.py
Library   TestCases/TrackWithVideoLesson.py
Library   TestCases/TrackWithVidLessonDocLesssonQuesLesson.py
Library   TestCases/LessonCreateDocument.py
Library   TestCases/LessonCreateQuestion.py
Library   TestCases/LessonCreateText.py
Library   TestCases/TrackWithImgLessonVidLesson.py
Library   TestCases/TrackWithTxtLessonImgLesson.py
Library   TestCases/TrackWithTxtVidQueLesson.py
Library   TestCases/TrackWithVidDocQueLesson.py
Library   TestCases/TrackWithAllCardsOne.py
Library   TestCases/TrackWithAllCardsTwoTimes.py
Library   TestCases/TrackWithFourLessons.py
Library   TestCases/TrackWithFourLessonsDifferentCombiOfLessons.py
Library   TestCases/TrackWithFourLessonsDifferentCombiOfLessons2.py
Library   TestCases/TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons.py

Library   TestCases/Delete_Tags_Attributes_Lessons.py

Library   TestCases/DeleteLesson.py


*** Test Cases ***
TC0 - User Login
    User Login
 
TC1 - Delete_Tags_Attributes_Lessons
    Main Delete All
    
TC2 - BlankLessonFive
    Blank Lesson Five Main   

TC3 - BlankLessonFiveTwo
    Blank Lesson Five Two Main
    
TC4 - BlankLessonOne
    Blank Lesson One Main
    
TC5 - BlankLessonTen
    Blank Lesson Ten Main
    
TC6 - BlankLessonTwo
    Blank Lesson Two Main  
    
TC7 - LessonExplainAConcept
    Lesson Explain A Concept Main
    
TC8 - TeachASkill
    Teach A Skill Main
    
    
    
TC9 - CreateCreator
    Create Creator User And Validation

TC10 - CreateLearner
    Create Learner User And Validation

TC11 - CreateLearnerAdministrator
    Create Learner Admin User And Validation
    
TC12 - CreateMasterAdmin
    Create Master Admin User And Validation
 
TC13 - UserAttributeListWithReq
    Create List Attribute With Required Field
    
TC14 - UserAttributeListWithoutReq
    Create List Attribute Without Required Field
           
TC15 - UserAttributeNumWithReq
    Create Number Attribute With Req
    
TC16 - UserAttributeNumWithoutReq
    Create Number Attribute Without Req
    
TC17 - UserAttributeTextWithReq
    Create Text Attribute With Req
    
TC18 - UserAttributeTextWithoutReq
    Create Text Attribute Without Req
    
TC19 - UserAttributeCheckboxWithReq
    Create Check Box Attribute With Req
    
TC20 - UserAttributeWithoutCheckbox
    Create Check Box Attribute Without Req
    
TC21 - UserAttributeDateWithReq
    Create Date Attribute With Req
    
TC22 - UserAttributeDateWithoutReq
    Create Date Attribute Without Req
    
TC23 - UserAttributeWithEmail
    Create Email Attribute With Req
    
TC24 - UserAttributeWithoutEmail
    Create Email Attribute Without Req

TC25 - LessonCreateImage
    Lesson With Image Upload Card
    
TC26 - LessonCreateVideo
    Lesson With Video Upload Card
    
TC27 - UserAttributeUserReferenceWithReq
    Create User Reference Attribute With Required Field
    
TC28 - UserAttributeUserReferenceWithoutReq
    Create User Reference Attribute Without Required Field
    
TC29 - TrackWithVidLessonDocLesssonQuesLesson
    Track With Two Lessons Vid Doc Ques
    
TC30 - TrackWithDocumentLesson
    Lesson With Document Card
    
TC31 - TrackWithImageLesson
    Lesson With Image Card
        
TC32 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card
    
TC33 - TrackWithTextLesson
    Track With Lesson Contains Text Card
    
TC34 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card
    
TC35 - TrackWithVideoLesson
    Lesson With Video Card

TC36 - CreateTagDocLesson
    Creating Tag For Document Lesson
    
TC37 - CreateTagImageLesson
    Create Tag For Image Lesson
    
TC38 - CreateTagLessonCombinedLesson
    Create Tag For Combined Lesson
    
TC39 - CreateTagLessonExplainAconcept
    Create Tag For Lesson Explain A Concept

TC40 - CreateTagLessonIntroduceAtopic
    Create Tag For Lesson Introduce A Topic
    
TC41 - CreateTagLessonLimitedmultiplecardlesson_1
    Create Tag For Lesson Limited Multiple Card Lesson One
    
    
TC42 - CreateTagLessonLimitedmultiplecardlesson_2
    Create Tag For Lesson Limited Multiple Lesson Two
    
TC43 - CreateTagLessonLimitedmultiplecardlesson_3
    Create Tag For Lesson Limited Multiple Card Lesson Three
    
TC44 - CreateTagLessonMultiplecardlesson
    Create Tag For Lesson Multiple Card Lesson
    
TC45 - CreateTagLessonPowerpoint
    Create Tag For Lesson Power Point
    
TC46 - CreateTagLessonScorm
    Create Tag For Lesson Scorm
    
TC47 - CreateTagLessonTeachAskill   
    Create Tag For Lesson Teach A Skill
    
TC48 - CreateTagLessonTextLesson
    Create Tag For Lesson Textlesson
    
TC49 - CreateTagQuesLesson 
    Create Tag For Question Lesson
    
TC50 - CreateTagTrackLessonDocument   
    Create Tag For Track Lesson Document
    
TC51 - CreateTagTrackLessonFiveVideoDocumentQuestion  
    Create Tag For Track Lesson Five Video Document Question
    
TC52 - CreateTagTrackLessonImage  
    Create Tag For Track Lesson Image
    
    
TC53 - CreateTagTrackLessonOneTextImageVideoDocumentQuestion  
    Create Tag For Track Lesson One Text Image Video Document Question
    
    
TC54 - CreateTagTrackLessonQuestion
    Create Tag For Track Lesson Question
    
TC55 - CreateTagTrackLessonTenTextVideoQuestion
    Create Tag For Track Lesson Ten Text Video Question
    
TC56 - CreateTagTrackLessonTwoTextImageVideoDocumentQuestion
    Create Tag For Track Lesson Two Text Image Video Document Question
    
TC57 - CreateTagTrackLessonVideo
    Create Tag For Track Lesson Video
    
    
TC58 - CreateTagTrackWithfourlessons10_12_3
    Create Tag For Track With Four Lessons Ten Twelve Three
    
TC59 - CreateTagTrackWithfourlessons4_5_6_7
    Create Tag For Track With Four Lessons Four Five Six Seven

      
TC60 - CreateTagTrackWithfourlessons78910
    Create Tag For Track With Four Lesson Seven Eight Nine Ten
    
TC61 - CreateTagTrackWithonelesson_9
    Create Tag For Track With One Lesson Nine
    
TC62 - CreateTagTrackWiththreelessons_3_4_5
    Create Tag For Track With Three Lessons Three Four Five
    
TC63 - CreateTagTrackWiththreelessons_5_6_7
    Create Tag For Track With Three Lessons Five Six Seven
    
TC64 - CreateTagTracklessonFiveTextImageQuestion
    Create Tag For Track Lesson Five Text Image Question
    
TC65 - CreateTagTrackWithTwolessons_1_2
    Create Tag For Track With Two Lessons One Two
    
TC66 - CreateTagTrackWithTwolessons_2_3
    Create Tag For Track With Two Lessons Two Three

TC67 - CreateTagVideoLesson
    Create Tag For Video Lesson
   
    
TC68 - LessonCreateDocument 
    Lesson With Document Upload Card
       
TC69 - LessonCreateQuestion
    LessonCreateQuestion.Lesson With Question Answer Card
    
TC70 - LessonCreateText
    LessonCreateText.Lesson With Text Card
    
TC71 - TrackWithImgLessonVidLesson
    Track With Two Lessons Imgand Vid
    
TC72 - TrackWithTxtLessonImgLesson
    Track With Txt Lesson Image Lesson
    
TC73 - TrackWithTxtVidQueLesson
    Lesson With Text Video Question Card
    
TC74 - TrackWithVidDocQueLesson 
    Lesson With Video Document Question Card
    
TC75 - TrackWithAllCardsOne
    Track With All Cards

TC76 - TrackWithAllCardsTwoTimes
    Track With All Card Two Time
    
TC77 - TrackWithFourLessons
    Track With Four Lesson
    
TC78 - TrackWithFourLessonsDifferentCombiOfLessons
    Track With Four Lessons Diff Combi 1
    
TC79 - TrackWithFourLessonsDifferentCombiOfLessons2
    Track With Four Lessons Different Combi 2
    
TC80 - TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons
    Track With Ques All Card One And Two Time Lessons
    

    
    
    
    
    
    
    
    
    
    
    
    
