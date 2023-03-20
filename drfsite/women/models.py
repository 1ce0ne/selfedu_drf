from django.db import models

class Women(models.Model):
    """
    Известные женщины:
        title - заголовок
        content - описание
        time_create - время создания записи
        time_update - время обновления записи
        is_published - опубликована запись или нет
        cat - категория (ссылка на вторую модель)
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    """
    Категории:
        name - название категории
    """
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name