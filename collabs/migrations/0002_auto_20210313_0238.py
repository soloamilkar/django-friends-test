# Generated by Django 3.1.7 on 2021-03-13 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('languages', '0003_auto_20210307_1958'),
        ('collabs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collab',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='collab',
            name='frameworks',
            field=models.ManyToManyField(blank=True, related_name='collab', to='languages.Framework'),
        ),
        migrations.AddField(
            model_name='collab',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='github'),
        ),
        migrations.AddField(
            model_name='collab',
            name='languages',
            field=models.ManyToManyField(related_name='collab', to='languages.Language'),
        ),
        migrations.AddField(
            model_name='collab',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='collab',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='collab', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('collab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='collabs.collab')),
            ],
        ),
    ]
