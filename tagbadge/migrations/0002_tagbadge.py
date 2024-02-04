# Generated by Django 3.2.6 on 2022-01-04 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagbadge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('badge_type', models.CharField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=30)),
                ('tag_name', models.CharField(default='', max_length=30)),
                ('preBuild', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bade_position', models.CharField(choices=[('TAG', 'Tag'), ('BADGE', 'Badge')], default='', max_length=30)),
                ('url', models.URLField(blank=True, null=True)),
                ('answerIf_TagOf_A', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer')),
                ('awarded_to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awarded_to_user', to=settings.AUTH_USER_MODEL)),
                ('questionIf_TagOf_Q', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question')),
            ],
        ),
    ]
