from django.db import models

# Table Candidate

GENDER = {
    ("M","M"),
    ("F","F")
}

ROLES = {
    ("Frontend","Frontend"),
    ("Backend","Backend"),
    ("Fullstack","Fullstack"),
    ("Intern","Intern")
}

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, null=True,choices=GENDER)
    role = models.CharField(max_length=100 , null=True, choices=ROLES)

    def __str__(self):
        return self.name