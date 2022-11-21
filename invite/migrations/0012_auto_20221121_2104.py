# Generated by Django 3.2.16 on 2022-11-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0011_alter_guest_rsvp'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='dessert1_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='dessert2_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='dessert3_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='main1_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='main2_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='main3_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='starter2_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='starter3_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]