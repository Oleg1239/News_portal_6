from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_common_group(sender, instance, created, **kwargs):
    if created:  # если пользователь только что создан
        group, _ = Group.objects.get_or_create(name='common')  # получаем группу common, создаем, если ее нет
        instance.groups.add(group)  # добавляем пользователя в группу
