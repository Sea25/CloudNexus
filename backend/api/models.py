from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='running')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name