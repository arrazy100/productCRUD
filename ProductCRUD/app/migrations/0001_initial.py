# Generated by Django 4.1.4 on 2022-12-23 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorymodel')),
            ],
        ),
    ]
