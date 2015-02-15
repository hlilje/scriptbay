from django.db import models


class Script(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    code = models.CharField(max_length=8192)
    pub_date = models.DateTimeField('date published')
    changed_date = models.DateTimeField('date changed')
    #rating = models.FloatField(default=0)
    
    def __str__(self): return self.title


class Review(models.Model):
    script = models.ForeignKey(Script)
    comment_text = models.CharField(max_length=1024)
    rating = models.IntegerField(default=0)
