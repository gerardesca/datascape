from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, DeviceBaseModel, DeviceTCPBaseModel


class ModbusTCP(BaseModel, DeviceBaseModel, DeviceTCPBaseModel):
    
    class Meta:
        verbose_name = 'Modbus TCP Device'
        verbose_name_plural = 'Modbus TCP Devices'


    def __str__(self):
        return f"{self.name} ({self.hostname}:{self.port})"
    