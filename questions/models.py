from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import json
def get_default_user():
    try:
        return User.objects.first().id  # Returns the ID of the first user in the database
    except ObjectDoesNotExist:
        return None  # Handle the case where no users exist
        

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)  # Default user
    time_taken = models.IntegerField(default=0)  # Default time is 0 seconds
    marks_obtained = models.IntegerField(default=0)  # Default marks are 0
    wrong_answers = models.IntegerField(default=0)  # Default wrong answers are 0
    level = models.IntegerField(default=1)  # Default level is 1
    created_at = models.DateTimeField(auto_now=True)
    test_id= models.IntegerField(default=get_default_user)
    fullname = models.CharField(max_length=255, default="")  # Full name of the user

    data = models.TextField(default="")
    def set_data(self,data_list):
        self.data=json.dumps(data_list)
    def get_data(self):
        return json.loads(self.data)


    def __str__(self):
        return f"Test by {self.user.username}"

class Question(models.Model):
    test_id = models.IntegerField(default=get_default_user)
    data = models.TextField(default="")
    answer = models.TextField(default="")
    def set_data(self,data_list):
        self.data=json.dumps(data_list)
    def get_data(self):
        return json.loads(self.data)


   