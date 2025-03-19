from django.db import models


class Mebellar(models.Model):
    nomi = models.CharField(max_length=100)
    rasmi = models.ImageField(upload_to='images/', verbose_name="RASMI:")
    narxi = models.IntegerField(default=0)
    izoh = models.TextField(max_length=100)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = 'Mebellar'
        db_table = 'mebellar'
class Bolim(models.Model):
    nomi=models.CharField(max_length=100)
    rasmi=models.ImageField(upload_to='images/', verbose_name="RASMI:")
    izoh=models.TextField(max_length=100)
    yonalish=models.TextField(max_length=100)
    def __str__(self):
        return self.nomi
    class Meta:
        verbose_name_plural = 'Bolim'
        db_table = 'bolimlar'
class Postlar(models.Model):
    nomi=models.CharField(max_length=100)
    rasmi=models.ImageField(upload_to='images/', verbose_name="RASMI:")
    def __str__(self):
        return self.nomi
    class Meta:
        verbose_name_plural = 'Postlar'
        db_table = 'postlar'
class Izohlar(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    txt=models.TextField(max_length=100)
    def __str__(self):
        return self.email



