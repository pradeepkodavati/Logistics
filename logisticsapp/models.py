
from django.db import models
otservice=[('out of depot','out of depot'),
           ('on th route','on th route'),
           ('out of service','out of service'),
           ('on destination','on destination')]
teamss=[('TeamA','TeamA'),
           ('TeamB','TeamB'),
           ('TeamC','TeamC'),
           ('TeamD','TeamD')]
class routeLogistics(models.Model):
    vehicleNumber=models.CharField(max_length=200,null=True,unique=True)
    route = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200,choices=otservice)
    destination = models.CharField(max_length=200, null=True)
    team = models.CharField(max_length=200, null=True,choices=teamss)
