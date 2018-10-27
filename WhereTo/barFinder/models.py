from django.db import models

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(unique = True,max_length = 400,blank = True)
    address = models.CharField(max_length = 400,blank = True)
    zipcode = models.IntegerField(default = "43210")
    EST_TYPE_CHOICES = (
    ('R', 'Restaurant'),
    ('M', 'Music'),
    ('D', 'Dive'),
    ('K', 'Karaoke'),    
    ('C', 'Campus'),
    ('HE', 'High-End'),
    ('T', 'Themed'),
    ('DN', 'Dance'),
)
    est_type = models.CharField(max_length=2,
                                choices=EST_TYPE_CHOICES,blank = True)
    open_time = models.CharField(blank = True)
    close_time = models.CharField(blank = True)
    est_url = models.URLField(blank = True)
    def __str__(self):
        return self.establishment_text
    
class Deals(models.Model):
    est = models.ForeignKey(Establishment,
                               on_delete=models.CASCADE,
                               verbose_name="Establishment FK",
                               )
    start_time = models.CharField(blank = True)
    end_time = models.CharField(blank = True)
    item = models.CharField(max_length = 200,blank = True)
    size = models.CharField(blank = True,max_length = 100)
    cost = models.CharField(max_length = 10,blank = True)
    DAY_CHOICES = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),    
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
    ('8', 'Every Day')
)
    day = models.IntegerField(choices = DAY_CHOICES,blank = True)
    def __str__(self):
        return self.deals_text