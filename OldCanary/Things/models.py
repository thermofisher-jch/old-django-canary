from django.db import models


class Thing(models.Model):
    id = models.AutoField(auto_created=False, verbose_name="Id", primary_key=True)
    name = models.CharField(max_length=128)
    rank = models.CharField(max_length=1)
    suit = models.CharField(max_length=1, null=True)
    created = models.DateField(auto_now_add=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)

    def __str__(self):
        return self.rank + " of " + ("None" if self.suit is None else self.suit)
