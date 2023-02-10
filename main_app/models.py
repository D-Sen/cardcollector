from django.db import models
from django.urls import reverse

class Format(models.Model):
  name = models.CharField(max_length=50)
  requirements = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('formats_detail', kwargs={'pk': self.id})

class Deck(models.Model):
  name = models.CharField(max_length=50)
  game = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  formats = models.ManyToManyField(Format)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'deck_id': self.id})

class Card(models.Model):
  name = models.CharField(max_length=50)
  cardType = models.TextField(max_length=100)
  deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice #{self.get_meal_display()}
    return f"Card Name: {self.name} is type: {self.cardType}"



