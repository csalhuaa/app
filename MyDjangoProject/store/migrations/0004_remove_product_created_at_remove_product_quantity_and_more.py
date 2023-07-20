# Generated by Django 4.2.2 on 2023-07-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='store.product'),
        ),
    ]
