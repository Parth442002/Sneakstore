# Generated by Django 2.2.14 on 2020-07-20 17:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(max_length=100)),
                ('category_image', models.ImageField(upload_to='categories/')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=10, unique=True)),
                ('company_logo', models.ImageField(upload_to='company/')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('product_image', models.ImageField(upload_to='products/')),
                ('detail_text', models.TextField(max_length=300)),
                ('launch_date', models.DateField()),
                ('onsale', models.BooleanField(default=True)),
                ('price', models.PositiveIntegerField()),
                ('is_bestseller', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Company')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-launch_date'],
            },
        ),
    ]