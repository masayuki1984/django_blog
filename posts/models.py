from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


    # count the amount of letters
    def get_total(self):
        return len(self.content)