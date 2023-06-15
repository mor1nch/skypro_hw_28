from users.models import User
from django.db import models
from categories.models import Categories


class Ads(models.Model):
    STATUS_CHOICES = [
        (True, 'Опубликовано'),
        (False, 'Не опубликовано')
    ]
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False, max_length=5)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
