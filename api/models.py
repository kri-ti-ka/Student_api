from django.db import models

# Create your models here.
class Students(models.Model):
    GENDERS=(
        ("f","female"),
        ("m","male"),
        ("u","undisclosed")
    )
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=1, choices=GENDERS)
    email=models.EmailField(max_length=100)
    percentage=models.FloatField()

    institute=models.ForeignKey("Institute", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
    

class Institute(models.Model):
    TYPES=(
        ("c","college"),
        ("u", "university"),
        ("h", "highschool")
    )
    name=models.CharField(max_length=200)  
    institute_type=models.CharField(max_length=1,choices=TYPES)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name