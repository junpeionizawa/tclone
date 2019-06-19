from django.db import models

# Create your models here.

#index_newtweetテーブルに、指定のカラムの作成指示を出すことが可能になる
class NewTweet(models.model):
	tweet = models.CharField(max_length = 255)