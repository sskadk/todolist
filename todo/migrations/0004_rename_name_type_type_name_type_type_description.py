# Generated by Django 5.2.1 on 2025-06-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_description_todo_task_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='type_name',
        ),
        migrations.AddField(
            model_name='type',
            name='type_description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
