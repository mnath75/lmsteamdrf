import os
import random
from django.db import models


def upload_image_path_profile(instance, filename):
    new_filename = random.randint(1,9996666666)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "profile/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
    )
         

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext





class Home(models.Model):
    home_id=models.AutoField(primary_key=True,db_column='category_id')
    home_title=models.CharField('Title',max_length=255)
    home_slug=models.SlugField('slug',max_length=255,null=True)
    home_logo =models.ImageField(upload_to = upload_image_path_profile, default=None,null=True, blank = True)
 
    def __str__(self):
        return self.home_title
    


