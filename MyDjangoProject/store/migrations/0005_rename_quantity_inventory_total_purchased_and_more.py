# Generated by Django 4.2.2 on 2023-07-16 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_created_at_remove_product_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='quantity',
            new_name='total_purchased',
        ),
        migrations.AddField(
            model_name='inventory',
            name='total_sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
