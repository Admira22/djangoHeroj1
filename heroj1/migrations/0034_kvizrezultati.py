# Generated by Django 4.2.1 on 2023-05-31 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroj1', '0033_firstaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='KvizRezultati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brojTacnih', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heroj1.userprofile')),
            ],
        ),
    ]
