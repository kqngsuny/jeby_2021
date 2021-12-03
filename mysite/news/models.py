from django.db import models
from django.contrib.auth.models import User


class Keyword(models.Model):
    title = models.CharField(max_length=50, verbose_name="관리명", unique=False)
    content = models.CharField(max_length=100, verbose_name="키워드")
    mailing = models.BooleanField(default=False, verbose_name="메일발송")
    order = models.PositiveIntegerField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_title_author"
            )
        ]


class Site(models.Model):
    address = models.CharField(max_length=100, verbose_name="Address")
    description = models.CharField(max_length=100, verbose_name="Description")

    def __str__(self):
        return self.description