# Generated by Django 3.0 on 2020-05-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='django', unique=True),
            preserve_default=False,
        ),
    ]
