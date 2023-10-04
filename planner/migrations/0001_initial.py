# Generated by Django 4.2.1 on 2023-06-19 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('leads', '0001_initial'),
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reminder_type', models.CharField(blank=True, max_length=5, null=True)),
                ('reminder_time', models.IntegerField(blank=True, null=True, verbose_name='Reminder')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
            ],
            options={
                'verbose_name': 'Reminder',
                'verbose_name_plural': 'Reminders',
                'db_table': 'reminder',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PlannerEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='Event')),
                ('event_type', models.CharField(max_length=7, verbose_name='Type of the event')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Planned', 'Planned'), ('Held', 'Held'), ('Not Held', 'Not Held'), ('Not Started', 'Not Started'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Deferred', 'Deferred')], max_length=64, verbose_name='Status')),
                ('direction', models.CharField(blank=True, max_length=20)),
                ('start_date', models.DateField(default=None)),
                ('close_date', models.DateField(default=None, null=True)),
                ('duration', models.IntegerField(default=None, null=True, verbose_name='Durations')),
                ('priority', models.CharField(blank=True, max_length=10)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='event_assigned_users', to=settings.AUTH_USER_MODEL)),
                ('attendees_contacts', models.ManyToManyField(blank=True, related_name='attendees_contact', to='contacts.contact')),
                ('attendees_leads', models.ManyToManyField(blank=True, related_name='attendees_lead', to='leads.lead')),
                ('attendees_user', models.ManyToManyField(blank=True, related_name='attendees_user', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, choices=[(10, 'Account'), (13, 'Lead'), (14, 'Opportunity'), (11, 'Case')], limit_choices_to=models.Q(models.Q(('app_label', 'account'), ('id', 10), ('model', 'Account')), models.Q(('app_label', 'leads'), ('id', 13), ('model', 'Lead')), models.Q(('app_label', 'opportunity'), ('id', 14), ('model', 'Opportunity')), models.Q(('app_label', 'cases'), ('id', 11), ('model', 'Case')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_created_by', to=settings.AUTH_USER_MODEL)),
                ('reminders', models.ManyToManyField(blank=True, to='planner.reminder')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PlannerEvent',
                'verbose_name_plural': 'PlannerEvents',
                'db_table': 'planner_event',
                'ordering': ('-created_at',),
            },
        ),
    ]
