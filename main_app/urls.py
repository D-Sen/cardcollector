from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('decks/', views.decks_index, name='index'),
  path('decks/<int:deck_id>/', views.decks_detail, name='detail'),
  path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
  path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
  path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),
  path('decks/<int:deck_id>/add_card/', views.add_card, name='add_card'),
  path('decks/<int:deck_id>/assoc_format/<int:format_id>/', views.assoc_format, name='assoc_format'),

  path('formats/', views.FormatList.as_view(), name='formats_index'),
  path('formats/<int:pk>/', views.FormatDetail.as_view(), name='formats_detail'),
  path('formats/create/', views.FormatCreate.as_view(), name='formats_create'),
]
