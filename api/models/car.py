from django.db import models
from django.contrib.auth import get_user_model

class Car(models.Model):
  name = models.CharField(max_length=100)
  year = models.IntegerField()
  mileage = models.IntegerField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"My car is a '{self.year}' '{self.name}' with '{self.mileage}' miles."

  def as_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'year': self.year,
        'mileage': self.mileage
    }
