# Generated by Django 3.0.5 on 2021-01-18 18:09

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=120, unique=True, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Color Producto',
                'verbose_name_plural': 'Colores',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripcion producto')),
                ('man', models.BooleanField(default=True, verbose_name='Para Hombre')),
                ('woman', models.BooleanField(default=True, verbose_name='Para Mujer')),
                ('weight', models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Peso')),
                ('price_purchase', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Precio de Compra')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Venta')),
                ('main_image', models.ImageField(upload_to='producto', verbose_name='imagen principal')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 4')),
                ('video', models.URLField(blank=True, null=True, verbose_name='unboxin')),
                ('stok', models.PositiveIntegerField(default=0, verbose_name='Stok')),
                ('num_sales', models.PositiveIntegerField(default=0, verbose_name='Veces vendido')),
                ('colors', models.ManyToManyField(to='producto.Colors')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
