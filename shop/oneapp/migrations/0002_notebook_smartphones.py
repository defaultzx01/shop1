# Generated by Django 3.1.3 on 2020-11-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name Product')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Display Type')),
                ('resolution', models.CharField(max_length=255, verbose_name='Resolution')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Battery capacity')),
                ('ram', models.CharField(max_length=255, verbose_name='Ram')),
                ('sd', models.BooleanField(default=True)),
                ('sd_max_volume', models.CharField(max_length=255, verbose_name='Max Sd capacity')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Main cam')),
                ('frontal_cam_mp', models.CharField(max_length=255, verbose_name='Front cam')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name Product')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Display Type')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Processor Freq')),
                ('ram', models.CharField(max_length=255, verbose_name='Ram')),
                ('video', models.CharField(max_length=255, verbose_name='Video')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Time Without Charge')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]