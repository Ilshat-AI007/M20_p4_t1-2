from django.urls import path
from .views import song_view

urlpatterns = [
    path('', song_view, name='ru'),
    path('fr/', song_view, {'lang': 'fr'}, name='fr'),
    path('de/', song_view, {'lang': 'de'}, name='de'),
    path('es/', song_view, {'lang': 'es'}, name='es'),
]