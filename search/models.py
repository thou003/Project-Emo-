from django.db import models

# Create your models here.
class Emoticon(models.Model):
    service = models.CharField(max_length=45)
    title = models.CharField(max_length=45, blank=True, null=True)
    artist = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoticon'


class EmoticonDetail(models.Model):
    url = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoticon_detail'



class Likes(models.Model):
    idnum = models.CharField(db_column='idNum', primary_key=True, max_length=45)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'likes'
