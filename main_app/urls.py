from django.urls import path
from . import views
'''
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cards/', views.cards_index, name='index'),
  path('cards/<int:card_id>/', views.cards_detail, name='detail'),
  path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
  path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
  path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
  path('cards/<int:card_id>/add_deck/', views.add_deck, name='add_deck'),
]
'''
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('decks/', views.decks_index, name='index'),
  path('decks/<int:deck_id>/', views.decks_detail, name='detail'),
  path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
  path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
  path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),
  path('decks/<int:deck_id>/add_card/', views.add_card, name='add_card'),
]
