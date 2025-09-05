from django.db import models


class CommunityModel(models.Model):
    custom_id = models.AutoField(primary_key=True)
    communityurl = models.CharField()
    url = models.CharField()
    active_users = models.IntegerField()
    created = models.DateTimeField()
    description = models.CharField()
    name = models.CharField()
    token = models.CharField()
    user = models.CharField(default="asd")
    
