from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='images/avatars/', null=True,
                               blank=True)
    groups = models.ManyToManyField(Group,
                                    related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='custom_user_permissions')

    def __str__(self):
        return self.username


class Comment(models.Model):
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/posts', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    audio = models.FileField(upload_to='audios/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField()
    about_me = models.TextField()
    gender_choices = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('oter', 'Иной')
    )
    gender = models.CharField(max_length=8, choices=gender_choices)
    interest_choices = (
        ('artist', 'художник'),
        ('musician', 'музыкант'),
        ('poet', 'поэт'),
        ('writer', 'писатель'),
        ('dancer', 'танцор'),
        ('spectator', 'просто зритель')
    )
    interests = models.CharField(max_length=15, choices=interest_choices)
    subscription = models.IntegerField()
    subscribes = models.ManyToManyField('self', symmetrical=False)
    link_other_social_networks = models.TextField()
