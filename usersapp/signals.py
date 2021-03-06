from django.db.models.signals import post_save
from django.contrib.auth.models import  User
from django.dispatch import receiver
from .models import  profileModel
@receiver(post_save,sender=User)
def create_profilemodel(sender,instance,created,**kwargs):
    if  created:
        profileModel.objects.create(user=instance)
        
        
@receiver(post_save,sender=User)
def save_profilemodel(sender,instance,**kwargs):
    instance.profilemodel.save()
    