# Generated by Django 5.1.1 on 2025-01-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGillo', '0002_alter_customer_user_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
