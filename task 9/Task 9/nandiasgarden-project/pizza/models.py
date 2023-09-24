from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)

class Intern(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    date = models.DateField()
    worked_on = models.TextField()
    screenshot = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return f"Task by {self.intern.name} on {self.date}"
