# Generated by Django 3.2.11 on 2022-04-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizData', '0002_alter_language_lg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='answer_text',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Answer Text'),
        ),
    ]
