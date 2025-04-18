# Generated by Django 5.1.6 on 2025-04-04 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=100, unique=True)),
                ('ingredient_amount', models.IntegerField(max_length=10)),
                ('unit_mesurement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(to='web.ingredient')),
            ],
        ),
    ]
