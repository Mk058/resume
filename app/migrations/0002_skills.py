# Generated by Django 3.2.15 on 2022-11-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('percent', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['added'],
            },
        ),
    ]