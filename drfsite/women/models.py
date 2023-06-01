from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='category')

    def __str__(self):
        return f'{self.name}'


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title verb')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'
