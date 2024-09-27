from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(null=False)
    status = models.IntegerField(choices=[
        (0, 'to do'),
        (1, 'doing'),
        (2, 'done'),
])

    def __str__(self):
        return self.description
# Create your models here.
