# Generated by Django 3.2.6 on 2021-10-13 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]