# Generated by Django 3.2.11 on 2022-04-30 12:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ck_text', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
