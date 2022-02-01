from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
