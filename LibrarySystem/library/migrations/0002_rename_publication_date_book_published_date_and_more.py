# Generated by Django 5.1.7 on 2025-03-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='published_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
