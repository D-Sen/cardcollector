from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
'''
from .models import Card
from .forms import DeckForm
'''

from .models import Deck
from .forms import CardForm

cards = [
  {'name': 'Sacrifice', 'game': 'MTG', 'color': 'Black' },
  {'name': 'Warp Artifact', 'game': 'Magic the Gathering', 'color': 'Black' },
  {'name': 'Cemetary Gate', 'game': 'Magic the Gathering', 'color': 'Black' },
  {'name': 'Basal Thrull', 'game': 'Magic the Gathering', 'color': 'Black' },
  {'name': 'Ragman', 'game': 'Magic the Gathering', 'color': 'Black' },

]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def decks_index(request):
  decks = Deck.objects.all()
  return render(request, 'decks/index.html', {'decks':decks })


def decks_detail(request, deck_id):
  deck = Deck.objects.get(id=deck_id)
  card_form = CardForm()
  return render(request, 'decks/detail.html', {'deck':deck, 'card_form': card_form })

def add_card(request, deck_id):
  form = CardForm(request.POST)
  # validate the form
  if form.is_valid():
    new_card = form.save(commit=False)
    new_card.deck_id = deck_id
    new_card.save()
  return redirect('detail', deck_id=deck_id)

class DeckCreate(CreateView):
  model = Deck
  fields = ['name', 'game', 'color'] #__all__
  
class DeckUpdate(UpdateView):
  model = Deck
  fields = ['game', 'color']
  
class DeckDelete(DeleteView):
  model = Deck
  success_url = '/decks'


'''
def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', {'cards':cards })


def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  deck_form = DeckForm()
  return render(request, 'cards/detail.html', {'card':card, 'deck_form': deck_form })

def add_deck(request, card_id):
  form = DeckForm(request.POST)
  # validate the form
  if form.is_valid():
    new_deck = form.save(commit=False)
    new_deck.card_id = card_id
    new_deck.save()
  return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
  model = Card
  fields = ['name', 'game', 'color'] #__all__
  
class CardUpdate(UpdateView):
  model = Card
  fields = ['game', 'color']
  
class CardDelete(DeleteView):
  model = Card
  success_url = '/cards'
'''
