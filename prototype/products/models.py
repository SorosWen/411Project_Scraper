from django.db import models

# Create your models here.
class UserActivity(models.Model): 
    email = models.EmailField(max_length = 30, default = 'None')
    user_action = models.CharField(max_length = 30)
    activity_date = models.DateField('date published')
    search_value = models.CharField(max_length = 30)

    def __str__(self):
        return self.activity_date.strftime("%d-%b-%Y (%H:%M:%S.%f)") + " " + self.user_action + " " + self.search_value

    def get_info(self):
        return [self.activity_date.strftime("%d-%b-%Y (%H:%M:%S.%f)").replace('(00:00:00.000000)', ''), self.user_action, self.search_value]
