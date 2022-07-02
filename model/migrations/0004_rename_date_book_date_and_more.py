# Generated by Django 4.0.3 on 2022-05-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='email',
            new_name='Email',
        ),
        migrations.RemoveField(
            model_name='book',
            name='time',
        ),
        migrations.AddField(
            model_name='book',
            name='Time',
            field=models.CharField(choices=[('8:00 to 9:00', '8:00 to 9:00'), ('9:00 to 10:00', '9:00 to 10:00'), ('10:00 to 1:00', '10:00 to 1:00')], max_length=200, null=True),
        ),
    ]
