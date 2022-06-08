from random import shuffle
from django.db import models


# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.\
from Quiz.models import Qtype
from account.models import User
from course.models import Topic
from ckeditor.fields import RichTextField



class Dlevel(models.Model):
    dl_id = models.AutoField(primary_key=True, db_column='dl_id')

    dl_title = models.CharField('Title', max_length=255) 
    def __str__(self):
        return self.dl_title

class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class Language(models.Model):
    lg_id = models.AutoField(primary_key=True, db_column='lg_id')

    lg_title = models.CharField('Title', max_length=255) 

    def __str__(self):
        return self.lg_title



class Question(ObjectTracking):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['qu_id']
    qu_id = models.AutoField(primary_key=True, db_column='qu_id')
    qtype = models.ForeignKey(
        Qtype, related_name='qtype_question3',  on_delete=models.SET_NULL,null=True,default=None )

    difficulty = models.ForeignKey(
        Dlevel, related_name='dlavel_question3',  on_delete=models.SET_NULL,null=True,default=None )

    language = models.ForeignKey(
        Language, related_name='language_question3', on_delete=models.SET_NULL,null=True,default=None )

    reference = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,default=None , related_name='ques_user1',db_column='user')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True,default=None ,related_name='topic_question3')
    def __str__(self):
        return str(self.qu_id)


class Ques(ObjectTracking):
   
    qd_id = models.AutoField(primary_key=True, db_column='qd_id',default=None)
    qid = models.ForeignKey(Question, related_name='ques_qdes3', on_delete=models.SET_NULL,default=None,null=True)
    question_para = RichTextField(blank=True, null=True,default=None)
    question_text = RichTextField(blank=True, null=True,default=None)
    
    ques_lang = models.ForeignKey(Language, related_name='language_qdes3', on_delete=models.SET_NULL,default=None ,null=True)
    description = models.TextField('description', blank=True, null=True,default=None)
    solution = RichTextField('solution', blank=True, null=True,default=None)
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    
    def __str__(self):
        return self.question_text

    @property
    def choices(self):
        return self.choice_set.all()
class Choice(models.Model):
    question = models.ForeignKey(Ques, related_name='choices', on_delete=models.SET_NULL,default=None , null=True)
    language = models.ForeignKey(Language, related_name='choice_answer3',  on_delete=models.SET_NULL,default=None,null=True)
    answer_text = models.CharField( max_length=255, verbose_name=_("Answer Text"),default=None)
    is_right = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text


class TestLayout(models.Model):
    tl_id = models.AutoField(primary_key=True, db_column='tl_id')

    tl_title = models.CharField('Title', max_length=255) 
    def __str__(self):
        return self.tl_title  
TYPE_CHOICES = (
    ("Practice", "Practice"),
    ("Examination", "Examination")
)


class Testmake(ObjectTracking):
      te_id = models.AutoField(primary_key=True, db_column='te_id')
      user = models.ForeignKey(User, models.DO_NOTHING, related_name='test_user1',db_column='user')
      testName = models.CharField( max_length=255) 
      tags=models.CharField(max_length=255)
      noOfQuestions=models.PositiveIntegerField()
      totalMarks=models.PositiveIntegerField(null=True)
      hour=models.PositiveIntegerField() 
      minute=models.PositiveIntegerField() 
      testCategory= models.CharField(choices=TYPE_CHOICES , max_length = 20,default='1') 
      testLayout=models.ForeignKey(TestLayout, models.DO_NOTHING, related_name='test_TestLayout',db_column='test_layout')
      poolQuestion=models.BooleanField(default=False)
      freeAvailable=models.BooleanField(default=False)
      testShowFrom=models.DateTimeField('%d/%m/%y %H:%M')
      testEndON=models.DateTimeField(blank=True, null=True)
      def __str__(self):
        return self.testName

class TestSection(models.Model):
    ts_id=models.AutoField(primary_key=True, db_column='ts_id')
    testmake=models.ForeignKey(Testmake, models.DO_NOTHING, related_name='testSeection_testMake',db_column='testmake')
    sectionName=models.CharField( max_length=255) 
    hour=models.PositiveIntegerField(default=False)
    minute=models.PositiveIntegerField(default=False) 
    allowedSectionSwitching=models.BooleanField(default=False)
    skipSectionBeforeTimeOver=models.BooleanField(default=False)
    studentChoice=models.BooleanField(default=False)
    useSectionAsBreak=models.BooleanField(default=False)
    showPreviousSection=models.BooleanField(default=False)
    sectionInstruction=models.TextField( blank=True, null=True,default=None)
    def __str__(self):
        return self.sectionName             

class TestQuestion(ObjectTracking):
    tq_id=models.AutoField(primary_key=True, db_column='tq_id',default=None)
    testID=models.ForeignKey(Testmake, related_name='testm_testQ', on_delete=models.SET_NULL,default=None,null=True)

    sectionID=models.ForeignKey(TestSection, related_name='testSection_testQ', on_delete=models.SET_NULL,default=None,null=True)

    questionID=models.ForeignKey(Ques, related_name='Quest_testQ', on_delete=models.SET_NULL,default=None,null=True)

    rightMarks=models.FloatField()
    wrongMarks=models.FloatField()
    partialMarks=models.FloatField()
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='testQ_user1',db_column='user')

    
class TestInstruction(ObjectTracking) :
    ti_id=models.AutoField(primary_key=True, db_column='tq_id',default=None)
    testID=models.ForeignKey(Testmake, related_name='testmake_testIns', on_delete=models.SET_NULL,default=None,null=True)
    instructionName=models.TextField( blank=True, null=True,default=None)
    discription=models.TimeField(blank= True,null=True,default=True)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='testInstruction_user1',db_column='user')

TYPE_CHOICES1 = (
    ("All_Questions", "All_Questions"),
    ("Wrong_Questions", "Wrong_Questions")
)

TYPE_CHOICES2 = (
    ("Show_Solution_only_once", "Show_Solution_only_once"),
    ("Show_Solution_always", "Show_Solution_always")
)

TYPE_CHOICES3 = (
    ("Passing_Marks", "Set_Passing_Marks"),
    ("Passing_Percentage", "Set_Passing_Percentage")
)

TYPE_CHOICES4 = (
    ("ReAttempt_in_Days", "ReAttempt_in_Days"),
    ("ReAttempts_in_Hours", "ReAttempts_in_Hours")
)

TYPE_CHOICES5 = (
    ("Normal", "Normal"),
    ("Scientific", "Scientific")
)
TYPE_CHOICES6 = (
    ("UniLangual", "UniLangual"),
    ("Bilingual", "Bilingual")
)
TYPE_CHOICES7 = (
    ("For_Test", "For_Test"),
    ("For_Section", "For_Section")
)
TYPE_CHOICES8 = (
    ("on_only_image", "on_only_image"),
    ("all", "all")
)
TYPE_CHOICES9 = (
    ("Diagonal", "Diagonal"),
    ("horizontal", "horizontal")
)


    

    
class TestSetting(models.Model):
    ti_id=models.AutoField(primary_key=True, db_column='tq_id',default=None)
    testID=models.ForeignKey(Testmake, related_name='testmake_testSetting', on_delete=models.SET_NULL,default=None,null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='TestSetting_user1',db_column='user')
    shuffleOption=models.BooleanField()
    shuffleQuestion=models.BooleanField()
    skipShuffleOptionn=models.BooleanField()
    SelectSectionForOptions=models.ForeignKey(TestSection, related_name='testmake_testSection', on_delete=models.SET_NULL,default=None,null=True)
    SelectSectionForQuestion=models.ForeignKey(TestSection, related_name='testmake_testSectionQS', on_delete=models.SET_NULL,default=None,null=True)

    enableMovePrevious=models.BooleanField()
    groupByQtype=models.BooleanField()
    groupByTopic=models.BooleanField()
    groupByQtag=models.BooleanField()
    enableCalclator=models.BooleanField()
    calculatorOptions=models.CharField(choices=TYPE_CHOICES5 , max_length = 20,default='1')
    
    noOfAttempt=models.PositiveIntegerField(default=1)
    reAttemptoptions=models.CharField(choices=TYPE_CHOICES4 , max_length = 20,default='1')
    noOfReattempt=models.IntegerField()
    
    unlimitedAttempt=models.BooleanField()
    showTimeSpent=models.BooleanField()
    nextQuestionJumpTimer=models.BooleanField()
    lingualOption=models.CharField(choices=TYPE_CHOICES6 , max_length = 20,default='1')
    
    enableDragDrop=models.BooleanField()
 
    generateRank=models.BooleanField()
 
    rankBatchLevel=models.BooleanField()
 
    rankCourseLevel=models.BooleanField()
 
    enablePassing=models.CharField(choices=TYPE_CHOICES7 , max_length = 20,default='1')
    setGradeOptions=models.CharField(choices=TYPE_CHOICES3 , max_length = 20,default='1')
    setPassingMark=models.PositiveIntegerField()
    percentage=models.BooleanField()
    percentile=models.BooleanField()
    tScore=models.BooleanField()
    partialMarking=models.BooleanField()
    enableGreading=models.BooleanField()
    gradeAmax=models.IntegerField()
    gradeAmin=models.IntegerField()
 
    gradeBmax=models.IntegerField()
 
    gradeBmin=models.IntegerField()
 
    gradeCmax=models.IntegerField()
 
    gradeCmin=models.IntegerField()
 
    gradeDmax=models.IntegerField()
 
    gradeDmin=models.IntegerField()
 
    gradeEmax=models.IntegerField()
 
    gradeEmin=models.IntegerField()
 
    gradeFmax=models.IntegerField()
 
    gradeFmin=models.IntegerField()
 
    enableSolution=models.BooleanField()
    afterEachQuestion=models.BooleanField()
    afterEndDate=models.BooleanField()
    afterTestComplete=models.BooleanField()
    onSpecificDate=models.DateTimeField()
    solutionOptionns=models.CharField(choices=TYPE_CHOICES2 , max_length = 50,default='1')
    revealAnswerOptions=models.CharField(choices=TYPE_CHOICES1 , max_length = 50,default='1')
    randomTestGenerator=models.BooleanField()
    enableProcotring=models.BooleanField()
    liveProctoring=models.BooleanField()
    userInvigilator=models.TextField(max_length=200,default=None,null=True)
    videoRecordingProctoring = models.BooleanField()
    geoTagging=models.BooleanField()
    randomSelfiesNo=models.IntegerField()
 
    ipTagging=models.BooleanField()
    noiseDetection=models.BooleanField()
    saveLogs=models.BooleanField()
    multipleDisplays=models.BooleanField()
    faceRecognize=models.BooleanField()
    remoteAccessDisable=models.BooleanField()
    idCardScanning=models.BooleanField()
    enableKeyboardinTest=models.BooleanField()
    enableMouseScroll=models.BooleanField()
    enableMouseRight=models.BooleanField()
    enableWatermark=models.BooleanField()
    watermarkLogo=models.BooleanField()
    uploadWatermark=models.ImageField()
    textWatermark=models.TextField(max_length=200,)
    watermarkOption=models.CharField(choices=TYPE_CHOICES8 , max_length = 50,default='1')
    watermarkLayoutOption=models.CharField(choices=TYPE_CHOICES9 , max_length = 50,default='1')
    enableStudentFeedback=models.BooleanField()


# class Result(models.Model):
#     re_id=
#     user=
#     testID=
#     startDateAndTime=
#     endDateAndTime=
#     sectionID=
    
