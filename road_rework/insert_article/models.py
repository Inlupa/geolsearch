from django.db import models


class Article(models.Model):
    content = models.CharField(max_length=10000, blank=True, null=True)
    article_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    creator = models.IntegerField()
    article_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'article'

