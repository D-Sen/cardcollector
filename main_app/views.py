import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Deck, Format
from .forms import CardForm


# Create your views here.
def assoc_format(request, deck_id, format_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Deck.objects.get(id=deck_id).formats.add(deck_id)
  return redirect('detail', deck_id=deck_id)



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def decks_index(request):
  decks = Deck.objects.all()
  return render(request, 'decks/index.html', {'decks':decks })


def decks_detail(request, deck_id):
  deck = Deck.objects.get(id=deck_id)
  id_list = deck.formats.all().values_list('id')
  formats_deck_isnt_in = Format.objects.exclude(id__in=id_list)
  card_form = CardForm()
  return render(request, 'decks/detail.html', {'deck':deck, 'card_form': card_form, 'formats': formats_deck_isnt_in })

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
  fields = ['name', 'game', 'color']
  
class DeckUpdate(UpdateView):
  model = Deck
  fields = ['game', 'color']
  
class DeckDelete(DeleteView):
  model = Deck
  success_url = '/decks'

class FormatList(ListView):
  model = Format

class FormatDetail(DetailView):
  model = Format

class FormatCreate(CreateView):
  model = Format
  fields = '__all__'


def assoc_format(request, deck_id, format_id):
  Deck.objects.get(id=deck_id).formats.add(format_id)
  return redirect('detail', deck_id=deck_id)
