# Generated by Django 4.2.6 on 2023-10-25 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_remove_todo_task_add_task_todo_alter_add_task_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_task',
            name='todo',
        ),
        migrations.AlterField(
            model_name='add_task',
            name='id',
            field=models.PositiveIntegerField(default=548, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.PositiveIntegerField(default=9480, primary_key=True, serialize=False),
        ),
    ]