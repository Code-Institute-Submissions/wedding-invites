# Generated by Django 3.2.16 on 2022-11-07 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invite', '0007_alter_guest_linked_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='couple',
            field=models.ManyToManyField(limit_choices_to=2, related_name='_invite_wedding_couple_+', to='invite.Wedding'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='user_id',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
