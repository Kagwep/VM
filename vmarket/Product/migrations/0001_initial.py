# Generated by Django 3.2.9 on 2022-02-22 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='name of product')),
                ('product_category', models.CharField(choices=[('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics')], max_length=100, verbose_name='product category')),
                ('product_subcategory', models.CharField(choices=[('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics'), ('Electronics', 'Electronics')], max_length=100, verbose_name='product subcategory')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=50, verbose_name='Product price')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shop')),
            ],
        ),
    ]