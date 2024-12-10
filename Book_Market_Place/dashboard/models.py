from django.db import models

gender_Choises = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]

class Profile_Model(models.Model):
    user_name = models.CharField(max_length=20)
    dob = models.DateField()
    user_email = models.EmailField()
    gender = models.CharField(max_length=1,choices=gender_Choises)
    profile_image = models.ImageField(upload_to='photo/',blank=True,null=True)
    
    def __str__(self):
        return self.user_name
    
