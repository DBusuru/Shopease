# Generated by Django 5.1.3 on 2024-11-26 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopease', '0003_newsletter_alter_review_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='date_added',
        ),
    ]
