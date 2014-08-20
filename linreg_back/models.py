from django.db import models

class Point(models.Model):
    input_number = models.IntegerField(default=0)
    posx = models.IntegerField(default=0)
    posy = models.IntegerField(default=0)

    def __str__(self):
        return str(self.posx) + " " + str(self.posy)
    
