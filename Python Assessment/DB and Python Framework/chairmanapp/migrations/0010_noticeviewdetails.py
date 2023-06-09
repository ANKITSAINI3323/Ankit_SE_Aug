# Generated by Django 4.1.6 on 2023-02-24 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0009_remove_chairman_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.notice')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
    ]