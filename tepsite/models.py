from django.db import models


from django.utils.encoding import python_2_unicode_compatible




class Program(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
 
    
 

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
    







		







				
