# Generated by Django 2.0.1 on 2018-01-30 14:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20180130_1404'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookbookmark',
            unique_together={('book', 'user')},
        ),
    ]