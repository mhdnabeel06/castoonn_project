# Generated by Django 4.1 on 2023-07-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=50)),
                ('experience', models.IntegerField(null=True)),
            ],
        ),
    ]