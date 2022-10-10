from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class RegistrationClass(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    dob = models.DateField()
    message = models.TextField()

    class Meta:
        db_table = 'web_registration'
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')

    def __unicode__(self):
        return self.name
