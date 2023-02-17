from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='photos/users', blank=True,  verbose_name='Фотография')
    age = models.SmallIntegerField(verbose_name='Возраст клиента', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('customusers:detail_user', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
