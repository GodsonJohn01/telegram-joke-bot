from jokebot import utility
import json
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import JokeBotUser
from .utility import get_chat_id, get_message, get_user, get_jokes, send_response


# Create your views here.
class JokeBotView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            message = get_message(data)
            chat_id = get_chat_id(data)
            username = get_user(data)
        except:
            message = username = None

        if message:
            msg = get_jokes(message)
            send_response(msg, chat_id)

        if username:
            user, _ = JokeBotUser.objects.get_or_create(
                user_id=chat_id, first_name=username, joke=message)
            user.count += 1
            user.save()

        return JsonResponse({"ok": "POST request processed"})


class UserListView(ListView):
    model = JokeBotUser
    paginate_by = 10
    template_name = "user_analytics.html"
    context_object_name = 'users'
    ordering = ['-count']
