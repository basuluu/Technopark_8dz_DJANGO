from django.db import models
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Post(models.Model, HitCountMixin):
    id_post = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    vision = models.BooleanField(default=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    hit_count_generic = GenericRelation(
     HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

class Comment(models.Model):
    id_сomment = models.AutoField(primary_key=True)
    id_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
