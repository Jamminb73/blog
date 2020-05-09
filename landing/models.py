from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

# Create your models here.
class HomeText(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = RichTextField(blank=True)

    def __str__(self):
        return self.title
