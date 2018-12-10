# Generated by Django 2.1.3 on 2018-12-10 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_department_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(default='1', max_length=450),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='img',
            field=models.CharField(default='1', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='clinic.Department'),
        ),
    ]