from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class note(models.Model):
    text=models.CharField(max_length=5000)
    complete = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

