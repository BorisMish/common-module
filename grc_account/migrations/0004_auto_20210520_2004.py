# Generated by Django 3.1 on 2021-05-20 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grc_account', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grc_account.account', verbose_name='social_account'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grc_account.account'),
        ),
    ]
