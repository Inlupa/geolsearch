from django.db import models

class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=-1, blank=True, null=True)
    article_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
