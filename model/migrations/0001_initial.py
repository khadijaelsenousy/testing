# Generated by Django 4.0.3 on 2022-05-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('CH_id', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Amount', models.CharField(max_length=200, null=True)),
                ('Description', models.TextField(null=True)),
                ('CodeForDiscond', models.IntegerField()),
                ('Total', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalSpecialistes',
            fields=[
                ('Sid', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('Sname', models.CharField(max_length=200, null=True)),
                ('Spassword', models.CharField(max_length=100, null=True)),
                ('Sphone', models.IntegerField()),
                ('Semail', models.EmailField(max_length=100, null=True)),
                ('Saddress', models.CharField(max_length=100, null=True)),
                ('Signature', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('Id', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('UserName', models.CharField(max_length=200, null=True)),
                ('Password', models.CharField(max_length=100, null=True)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Process', models.CharField(max_length=100, null=True)),
                ('Disease_history', models.TextField(null=True)),
            ],
        ),
    ]