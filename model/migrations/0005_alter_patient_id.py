# Generated by Django 4.0.3 on 2022-06-12 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_rename_date_book_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Id',
            field=models.CharField(auto_created=True, max_length=10, primary_key=b'I01\n', serialize=False),
        ),
    ]
