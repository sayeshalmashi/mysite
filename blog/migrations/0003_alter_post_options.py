# Generated by Django 3.2.25 on 2024-04-05 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240403_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-creat_date']},
        ),
    ]
