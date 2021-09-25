# telegram-joke-bot
This is a simple telegram joke bot using Django.


Steps to deploy the project locally:

1. Clone the Repository `https://github.com/GodsonJohn01/telegram-joke-bot.git`. Then `cd telegram-joke-bot`

1. Install and activate virtualenv: `pip install virtualenv`, `virtualenv venv`, `source venv/bin/activate`

3. Install the requirements using `pip install -r requirements.txt`

2. Create environment variable file `.env` based on the `.env.example` file in the project's root directory
   We are using Postgresql DB, create user and database:
          `sudo -u postgres createuser -sPE user_name`
          `sudo -u postgres createdb db_name`
  Get your bot token:
          Talk to the BotFather and get and set your bot token
          Open telegram, and search for the Botfather. Type the command `/newbot` to create a bot and follow the instructions to get a token.

4. Migrate the tables to the database: `python manage.py migrate`
5. Create Superuser: `python manage.py createsuperuser`
6. And start the server with `python manage.py runserver`. Go to http://127.0.0.1:8000/joke-bot/users/ on your browser. Django Admin: http://127.0.0.1:8000/admin

7. Take a new tab on your terminal and start it with `ngrok http 8000`. Download ngrok (https://ngrok.com/)
   You will get a ngrok https url. eg: https://c4fd-45-115-91-243.ngrok.io
   This URL we will be used to set up the WebHook.

8. Set your webhook to connect to the Telegram API
- `https://api.telegram.org/bot<BOT-TOKEN>/setWebhook?url=<https://c4fd-45-115-91-243.ngrok.io>/`
   Replace variables in the < > with your credentials.

   Response to following the link should be like:
   {"ok":true,"result":true,"description":"Webhook was set"}

Congrats, it’s alive!
If everything is right, you should now be able to talk to the bot.
