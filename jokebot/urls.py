from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import JokeBotView, UserListView

urlpatterns = [
    path('', csrf_exempt(JokeBotView.as_view()), name='joke-bot'),
    path('joke-bot/users/', UserListView.as_view(), name='joke-bot-user')
]