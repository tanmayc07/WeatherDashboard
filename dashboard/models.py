from django.db import models


class CityModel(models.Model):
    city_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name
