from django.db import models

# Create your models here.
class JokeBotUser(models.Model):

    STUPID = 'stupid'
    FAT = 'fat'
    DUMB = 'dumb'
    JOKES = [
        (STUPID, 'stupid'),
        (FAT, 'fat'),
        (DUMB, 'dump'),
    ]
    joke = models.CharField(
        choices=JOKES, 
        max_length=10, 
        default=STUPID,
    )
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.first_name
