from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    git_link = models.CharField(max_length = 200)
    small_des = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to = 'image/')
    added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added']


class Skills(models.Model):
    subject = models.CharField(max_length=100)
    percent = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['added']