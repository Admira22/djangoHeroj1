# Generated by Django 4.2 on 2023-04-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroj1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date publiched')),
                ('title', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('text', models.CharField(max_length=2000)),
                ('image', models.ImageField(height_field='height', max_length=255, upload_to='images/', width_field='width')),
            ],
        ),
    ]
