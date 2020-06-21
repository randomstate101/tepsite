from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



from django.utils.encoding import python_2_unicode_compatible





class Program(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')

)
ANSWER_CHOICES=(
     ('Strongly Disagree','Strongly Disagree'),
     ('Disagree','Disagree'),
     ('Neutral','Neutral'),
     ('Agree','Agree'),
     ('Strongly Agree', 'Strongly Agree'),
)


class ProgramFeedbackForm(models.Model):
    intern_name = models.CharField(max_length=30,blank=True,null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    program = models.ForeignKey(Program,blank=True,null=True, on_delete= models.CASCADE)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Overall_my_impression_of_this_course_was_excellent = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_objectives_were_clearly_stated_and_used_understandable_terms=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_met_the_defined_objectives = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Both_the_facility_and_equipment_used_met_all_needs_of_the_course = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_materials_were_both_useful_and_easy_to_follow  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_demonstrated_thorough_knowledge_and_understanding_of_the_topic = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_presented_information_in_a_clear_understandable_and_professional_manner= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_amount_of_time_scheduled_for_this_course_was_exactly_what_was_needed_to_meet_the_objectives= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_relates_directly_to_my_current_job_responsibilities = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_would_recommend_this_course_to_other_teammates  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    details = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.intern_name








class Feedback(models.Model):
    intern_name = models.CharField(max_length=120)
    email = models.EmailField()
    program = models.ForeignKey(Program, on_delete= models.CASCADE)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.intern_name




LEVEL_CHOICES = (
     ('warning', 'Warning'),
     ('error', 'Error'),
     ('success', 'Success'),
     ('info', 'Info'),
)

class Announcement(models.Model):
    """
    Model to hold global announcements
    """
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7,
                choices=LEVEL_CHOICES, default='info')

    def __unicode__(self):
        return self.body[:50]
