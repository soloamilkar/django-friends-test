# Generated by Django 3.1.7 on 2021-03-13 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collabs', '0002_auto_20210313_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collab',
            name='status',
            field=models.CharField(choices=[('lfg', 'Looking For Group'), ('progress', 'In progress'), ('done', 'Done')], default=('lfg', 'Looking For Group'), max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]