# Generated by Django 4.0.3 on 2023-06-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_portfolio_remove_my_detail_main_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('header', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=500)),
            ],
        ),
    ]
