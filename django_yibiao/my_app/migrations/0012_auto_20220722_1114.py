# Generated by Django 3.2.12 on 2022-07-22 03:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_alter_admin_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2022, 7, 22, 3, 14, 50, 393825, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.CreateModel(
            name='WellDanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgRec', models.FileField(max_length=128, upload_to='yolov5-master/number/', verbose_name='识别图片')),
                ('imgResult', models.CharField(max_length=128, verbose_name='识别结果')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.admin', verbose_name='用户')),
            ],
        ),
    ]