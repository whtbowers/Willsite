# Generated by Django 2.0.2 on 2018-02-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('align', '0012_auto_20180216_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pairedjob',
            name='date',
        ),
        migrations.AddField(
            model_name='pairedjob',
            name='readsfile1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='pairedjob',
            name='readsfile2',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
