# Generated by Django 5.1.4 on 2024-12-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0003_alter_hall_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
