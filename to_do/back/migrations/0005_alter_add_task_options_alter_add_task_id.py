# Generated by Django 4.2.6 on 2023-10-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0004_alter_add_task_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='add_task',
            options={'ordering': ['done']},
        ),
        migrations.AlterField(
            model_name='add_task',
            name='id',
            field=models.PositiveIntegerField(default=220, primary_key=True, serialize=False),
        ),
    ]
