# Generated by Django 3.2.9 on 2021-11-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(max_length=10),
        ),
    ]