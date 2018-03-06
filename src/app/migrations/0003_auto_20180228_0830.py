# Generated by Django 2.0.2 on 2018-02-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180228_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='app.Post'),
        ),
    ]
