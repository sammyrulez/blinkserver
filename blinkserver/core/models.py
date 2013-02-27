from django.db import models
from django.contrib.auth.models import User

class Hook(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    private = models.BooleanField()

    def __str__(self):
        return self.name

class BlinkStatus(models.Model):
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
    hook =models.ForeignKey(Hook)
    fading_time = models.FloatField(blank=True, null=True)
    duration = models.FloatField()
    position = models.PositiveSmallIntegerField("Position")
    def __str__(self):
        return "Blink Status %d for %s" %(self.position,self.hook.name)
    class Meta:
        ordering = ('position', )
        verbose_name_plural = "Blink Statuses"
