# Generated by Django 4.1.6 on 2023-02-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
