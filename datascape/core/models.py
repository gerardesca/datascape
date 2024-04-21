from django.utils.translation import gettext_lazy as _
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('date created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('last updated'))

    class Meta:
        abstract = True
        

class DeviceType(models.Model):
    name = models.CharField(verbose_name=_('device type'), max_length=200, unique=True)
    app_name = models.CharField(verbose_name=_('app name'), max_length=400)
    device_class = models.CharField(verbose_name=_('device class'), max_length=400, blank=False)
    daq_daemon = models.BooleanField(verbose_name=_('daq daemon'), default=True)
    single_thread = models.BooleanField(verbose_name=_('single thread'), default=True)
    
    def __str__(self):
        return self.name
    
   
class DeviceBaseModel(models.Model):
    name = models.CharField(verbose_name=_('device name'), max_length=200, unique=True)
    description = models.CharField(verbose_name=_('description'), max_length=500, blank=True)
    active = models.BooleanField(verbose_name=_('enabled'), default=True, help_text=_('default: True'))
    device_type = models.ForeignKey(DeviceType, verbose_name=_('device type'), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        
        
class DeviceTCPBaseModel(models.Model):
    hostname = models.GenericIPAddressField(verbose_name=_('host'), default="127.0.0.1", protocol='IPv4')
    port = models.PositiveIntegerField(verbose_name=_('port'), validators=[MinValueValidator(1), MaxValueValidator(65535)])
    local_address = models.GenericIPAddressField(verbose_name=_('local address'), protocol='IPv4', blank=True, null=True)
    timeout = models.FloatField(verbose_name=_('timeout'), default=2000)
    
    class Meta:
        abstract = True