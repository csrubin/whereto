from django.db import models

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(unique = True)
    address = models.CharField()
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
    est_type = models.CharField(max_length = 2,choices=EST_TYPE_CHOICES)
    open_time = models.IntegerField(blank = True)
    close_time = models.IntegerField(blank = True)
    est_url = models.URLField(blank = True)
    
class Deals(models.Model):
    est = models.ForeignKey(Establishment,
                               on_delete=models.CASCADE,
                               verbose_name="Establishment FK",
                               )
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    item = models.CharField()
    size = models.CharField(blank = True)
    cost = models.CharField()
    DAY_CHOICES = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),    
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)
    day = models.IntegerField(choices = DAY_CHOICES)