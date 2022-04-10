from django.db import models


# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.\
from Quiz.models import Qtype
from account.models import User
from course.models import Topic

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
        Qtype, related_name='qtype_question3', on_delete=models.DO_NOTHING)

    difficulty = models.ForeignKey(
        Dlevel, related_name='dlavel_question3', on_delete=models.DO_NOTHING)

    language = models.ForeignKey(
        Language, related_name='language_question3', on_delete=models.DO_NOTHING)

    reference = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='ques_user1',db_column='user')
    topic = models.ForeignKey(Topic, models.DO_NOTHING,related_name='topic_question3')
    def __str__(self):
        return str(self.qu_id)


class Ques(ObjectTracking):
   
    qd_id = models.AutoField(primary_key=True, db_column='qd_id',default=None)
    qid = models.ForeignKey(Question, related_name='ques_qdes3', on_delete=models.DO_NOTHING,default=None)
    question_para = models.TextField(blank=True, null=True,default=None)
    question_text = models.TextField(blank=True, null=True,default=None)
    
    ques_lang = models.ForeignKey(Language, related_name='language_qdes3', on_delete=models.DO_NOTHING,default=None)
    description = models.TextField('description', blank=True, null=True,default=None)
    solution = models.TextField('solution', blank=True, null=True,default=None)
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    
    def __str__(self):
        return self.question_text

    @property
    def choices(self):
        return self.choice_set.all()
class Choice(models.Model):
    question = models.ForeignKey(Ques, related_name='choices',on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, related_name='choice_answer3', on_delete=models.DO_NOTHING,default=None)
    answer_text = models.CharField( max_length=255, verbose_name=_("Answer Text"),default=None,null=True,blank=True)
    is_right = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text
