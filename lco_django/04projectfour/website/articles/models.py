from django.db import models

class Articles(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE )
    title = models.CharField(max_length=50)
    text =  models.TextField()


    def __str__(self):
        return self.title