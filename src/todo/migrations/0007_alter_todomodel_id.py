# Generated by Django 5.1.3 on 2024-11-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todomodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]