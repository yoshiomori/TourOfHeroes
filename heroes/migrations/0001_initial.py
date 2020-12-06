# Generated by Django 3.1.3 on 2020-11-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddIndex(
            model_name='hero',
            index=models.Index(fields=['name'], name='heroes_hero_name_2f7a12_idx'),
        ),
    ]