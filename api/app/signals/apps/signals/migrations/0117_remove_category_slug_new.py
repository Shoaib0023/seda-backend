# Generated by Django 2.2.13 on 2020-07-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0116_category_slug_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug_new',
        ),
    ]