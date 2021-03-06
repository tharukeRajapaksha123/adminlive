# Generated by Django 3.2.9 on 2021-11-14 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_auto_20211114_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='layout',
            field=models.IntegerField(choices=[(1, 'Layout 1'), (2, 'Layout 2'), (3, 'Layout 3'), (4, 'Layout 4'), (5, 'Layout 5')], default=1),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='screen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_admin.screen'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='screen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_admin.screen'),
        ),
    ]
