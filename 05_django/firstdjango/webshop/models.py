from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    quantity = models.IntegerField(default=0)

    def sell(self):
        if self.quantity > 0:
            self.quantity -= 1
            return self.save()
        else:
            return 0

    def __str__(self):
        return "{} {}".format(self.title, self.quantity)
