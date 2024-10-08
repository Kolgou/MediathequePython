# Generated by Django 5.1 on 2024-09-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_rename_author_media_auteur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvd',
            name='media_ptr',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='media_ptr',
        ),
        migrations.RemoveField(
            model_name='media',
            name='date_publication',
        ),
        migrations.AddField(
            model_name='media',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='media',
            name='type',
            field=models.CharField(choices=[('Livre', 'Livre'), ('CD', 'CD'), ('DVD', 'DVD')], default='Livre', max_length=50),
        ),
        migrations.AlterField(
            model_name='media',
            name='auteur',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='media',
            name='titre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='nom',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Cd',
        ),
        migrations.DeleteModel(
            name='Dvd',
        ),
        migrations.DeleteModel(
            name='Livre',
        ),
    ]
