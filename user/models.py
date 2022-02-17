from django.db import models

# Create your models here.
class Emoticon(models.Model):
    service = models.CharField(max_length=45)
    title = models.CharField(max_length=45, blank=True, null=True)
    artist = models.CharField(max_length=20, blank=True, null=True)
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


class EmoticonOk(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    artist = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    canceldate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoticon_ok'


class Likes(models.Model):
    idnum = models.CharField(db_column='idNum', primary_key=True, max_length=45)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    id = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'likes'





class Member(models.Model):
    idnum = models.AutoField(db_column='idNum', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    birth = models.DateField(db_column='Birth')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='Phonenumber', max_length=11)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.
    id = models.CharField(db_column='Id', max_length=45)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'member'


class Refund(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    refunddate = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund'


class Sell(models.Model):
    idNum = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    id = models.CharField(max_length=45)


    class Meta:
        managed = True
        db_table = 'sell'
