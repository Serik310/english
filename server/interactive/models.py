from django.db import models


class Word(models.Model):
    name = models.TextField()
    transcription = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
