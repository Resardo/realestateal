# Generated by Django 4.0.4 on 2022-04-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronat', '0006_remove_apartment_slug_remove_garage_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(help_text='Vendos pershkrimin', max_length=1000, verbose_name='Pershkrimi'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.TextField(help_text='Vendos titullin e njoftimit', max_length=500, verbose_name='Titulli'),
        ),
    ]