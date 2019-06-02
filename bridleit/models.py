import json
from django.contrib.postgres.fields import JSONField
from django.db import models


class Word(models.Model):
    guess_word = models.CharField(max_length=100)
    taboo_words = models.CharField(max_length=100)
    data = JSONField(null=True, editable=False)

    def save(self, *args, **kwargs):
        taboo_words_list = self.taboo_words.split(",")
        taboo_words_list = [i.strip() for i in taboo_words_list]

        data_dict = {
            'guessWord': self.guess_word,
            'tabooWords': taboo_words_list
        }

        self.data = json.dumps(data_dict)
        super(Word, self).save(*args, **kwargs)
