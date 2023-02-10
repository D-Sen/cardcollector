from django.db import models
from django.urls import reverse

# Create your models here.
'''
class Card(models.Model):
  name = models.CharField(max_length=50)
  game = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'card_id': self.id})

class Deck(models.Model):
  name = models.CharField(max_length=50)
  colors = models.TextField(max_length=100)
  card = models.ForeignKey(Card, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice #{self.get_meal_display()}
    return f"Deck Name: {self.name} uses colors: {self.colors}"
'''

class Deck(models.Model):
  name = models.CharField(max_length=50)
  game = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'deck_id': self.id})

class Card(models.Model):
  name = models.CharField(max_length=50)
  colors = models.TextField(max_length=100)
  deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice #{self.get_meal_display()}
    return f"Card Name: {self.name} is colors: {self.colors}"
