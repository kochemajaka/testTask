# Generated by Django 4.2.1 on 2023-09-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_alter_access_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='userID',
            field=models.IntegerField(),
        ),
    ]