from django.db import models


class Script(models.Model):
    code = models.CharField(max_length=8192)
    #rating = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published')
    changed_date = models.DateTimeField('date changed')

class Review(models.Model):
    script = models.ForeignKey(Script)
    comment_text = models.CharField(max_length=1024)
    rating = models.IntegerField(default=0)
