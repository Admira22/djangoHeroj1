# Generated by Django 4.2.1 on 2023-05-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroj1', '0032_alter_lekcija_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstAid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintitle', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=2000)),
                ('subtitle1', models.CharField(max_length=1000)),
                ('part1', models.CharField(max_length=2000)),
                ('subtitle2', models.CharField(max_length=2000)),
                ('part2', models.CharField(max_length=2000)),
                ('subtitle3', models.CharField(max_length=2000)),
                ('part3', models.CharField(max_length=2000)),
                ('subtitle4', models.CharField(max_length=2000)),
                ('part4', models.CharField(max_length=2000)),
                ('image', models.ImageField(max_length=255, upload_to='images/')),
            ],
        ),
    ]