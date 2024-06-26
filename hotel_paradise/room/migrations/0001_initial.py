# Generated by Django 5.0.6 on 2024-06-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=40)),
                ('bedroom_count', models.IntegerField()),
                ('bathroom_count', models.IntegerField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/img/room_images/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
