from django.db import models

# Create your models here.
class UserActivity(models.Model): 
    email = models.EmailField(max_length = 30, default = 'None')
    user_action = models.CharField(max_length = 30)
    activity_date = models.DateField('date published')
    search_value = models.CharField(max_length = 30)

    def __str__(self):
        return self.email + self.user_action + " " + self.activity_date.strftime("%d-%b-%Y (%H:%M:%S.%f)") + " " + self.search_value