# Generated by Django 5.0.3 on 2024-06-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serveyform', '0003_remove_surveyofficer_surver_officer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyofficer',
            name='surver_officer_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surveyofficer',
            name='surver_officer_number',
            field=models.CharField(max_length=13),
        ),
    ]