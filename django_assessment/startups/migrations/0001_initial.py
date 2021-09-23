# Generated by Django 3.2 on 2021-09-23 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_position', models.CharField(blank=True, max_length=128, null=True)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(blank=True, max_length=4, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescriptor_name', models.CharField(max_length=255)),
                ('prescriptor_position', models.CharField(blank=True, max_length=128, null=True)),
                ('prescriptor_email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=255)),
                ('website', models.URLField(blank=True, null=True)),
                ('one_liner', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('founded', models.CharField(blank=True, max_length=30, null=True)),
                ('money_raised_usd', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='startups', to='startups.country')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='startups.stage')),
            ],
        ),
    ]
