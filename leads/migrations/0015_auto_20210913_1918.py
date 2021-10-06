# Generated by Django 3.2 on 2021-09-13 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0034_auto_20210913_1918'),
        ('leads', '0014_auto_20210324_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.company'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='assigned_to',
            field=models.ManyToManyField(related_name='lead_assigned_users', to='common.Profile'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_created_by', to='common.profile'),
        ),
    ]
