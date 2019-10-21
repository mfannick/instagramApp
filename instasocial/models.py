# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     userBio=models.TextField()
#     userPic=models.ImageField(default='default.png',upload_to='profileImage/',blank=True)
#     userF=models.ForeignKey(User,on_delete=models.CASCADE)
#     profileTime=models.DateField(auto_now_add=True)

class Profile(models.Model):
    userF=models.ForeignKey(User,on_delete=models.CASCADE)
    userBio=models.TextField()
    userPic=models.ImageField(default='default.png',upload_to='profileImage/',blank=True)
    profileTime=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.userF.username


class Image (models.Model):
    image=models.ImageField(default='default.png',upload_to='images/')
    imageName=models.CharField(max_length=30,blank=True)
    imageCaption=models.CharField(max_length=30,blank=True)
    imageComment=models.TextField()
    # imageLike=models.IntegerField()
    imageTime=models.DateField(auto_now_add=True)
    userF=models.ForeignKey(User,on_delete=models.CASCADE)
    profileF=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.imageName

    @classmethod
    def searchImageByUser(cls,search_term):
        imageUser = cls.objects.filter(userF__username__icontains=search_term)
        return imageUser


# class Comment(models.Model):
#     commentWrite=models.TextField()
#     commentTime=models.DateField(auto_now_add=True)

# # class Follower(models.Model):
    
