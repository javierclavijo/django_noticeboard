from django.db import models


# Create your models here.


class Notice(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=40)
    # author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    exp_date = models.DateTimeField('Expiration date')
    body = models.TextField(max_length=500)
    # hidden = models.BooleanField(default=False)
    # attachment = models.FileField(blank=True)
