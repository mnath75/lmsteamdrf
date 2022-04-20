from django.db import models

# Create your models here.
class Image(models.Model):
   
    image_text = models.TextField(db_column='image_text',default=None,null=True)
    
    def __str__(self):
        return self.image_text

  