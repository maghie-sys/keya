import os
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Er(models.Model):
    Er_CODE = models.CharField(max_length=8)
    ErTh_CODE = models.CharField(max_length=8)
    # Fc_CODE = models.CharField(max_length=8)
    ErAd_CODE = models.CharField(max_length=8)
    Er_Name = models.CharField(max_length=20)
    Er_Num = models.CharField(max_length=20)
    # ErPic_CODE = models.CharField(max_length=8)
    Er_Grpt = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Er_Review = models.TextField(max_length=200)

class Th(models.Model):
    th = models.ForeignKey('Er', on_delete=models.CASCADE)
    Th_CODE = models.CharField(max_length=8)
    ErTh_CODE = models.CharField(max_length=8)
    #ThFc_CODE = models.CharField(max_length=8, primary_key=True)
    Th_Name = models.CharField(max_length=20)
    Th_Genre = models.CharField(max_length=20)
    Th_Diff = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Th_Fear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Th_Act = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Th_Intro = models.TextField(max_length=200)
    #ThGr_CODE = models.CharField(max_length=8)
    Th_Review = models.TextField(max_length=200)
    #Th_Pic1 = models.CharField(max_length=20)

class ThPic(models.Model):
    th = models.ForeignKey(Th, on_delete=models.CASCADE)
    Th_CODE = models.CharField(max_length=8)
    #ThPic_CODE = models.CharField(max_length=8)
    Th_pic = models.ImageField(default='/image/th/', upload_to='image/th/', blank=True, null=True)

class ThGr(models.Model):
    th = models.ForeignKey('Th', on_delete=models.CASCADE,max_length=8)
    ThGr_CODE = models.CharField(max_length=8)
    ThGr_pt = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ThGr_review = models.TextField(max_length=200)
    #ThGr_pic = models.CharField(max_length=8)

class ErAd(models.Model):
    #ErAd_CODE = models.CharField(primary_key=True, max_length=8, null=False)
    er = models.OneToOneField('Er', on_delete=models.CASCADE,max_length=8)
    ErAd_CODE = models.CharField(max_length=8)
    ErAd_Num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)]) # 우편번호
    ErAd_Add1 = models.CharField(max_length=20) # 도
    ErAd_Add2 = models.CharField(max_length=20) # 시
    ErAd_Add3 = models.CharField(max_length=20) # 구
    ErAd_Add4 = models.CharField(max_length=20) # 동 또는 도로명
    ErAd_Add5 = models.CharField(max_length=20) # 이후 주소

