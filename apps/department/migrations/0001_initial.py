# Generated by Django 4.0.2 on 2022-02-16 02:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of department', max_length=100)),
                ('uuid', models.UUIDField(default=uuid.UUID('87fb72a6-b9b2-4bc6-b8b0-a6a48017834f'), help_text='UUID of department', unique=True)),
            ],
        ),
    ]