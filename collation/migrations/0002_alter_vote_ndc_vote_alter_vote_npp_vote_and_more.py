# Generated by Django 4.1 on 2022-09-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='ndc_vote',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vote',
            name='npp_vote',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vote',
            name='other_vote',
            field=models.IntegerField(),
        ),
    ]