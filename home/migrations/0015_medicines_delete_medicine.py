# Generated by Django 4.2.6 on 2023-12-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_imagedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('patId', models.TextField()),
                ('email', models.TextField()),
                ('medicine', models.TextField()),
                ('message', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='medicine',
        ),
    ]