# Generated by Django 5.1 on 2024-09-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='author',
            new_name='auteur',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='published_date',
            new_name='date_publication',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='title',
            new_name='titre',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='phone_number',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='prenom',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='member',
            name='nom',
            field=models.CharField(default='Inconnu', max_length=255),
        ),
    ]
