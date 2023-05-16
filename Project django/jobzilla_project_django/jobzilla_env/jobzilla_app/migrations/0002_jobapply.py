# Generated by Django 4.1.7 on 2023-04-11 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobzilla_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobpost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.jobpost')),
                ('jobseeker_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.jobskeer_details')),
                ('jobseeker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.jobseeker')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.user')),
            ],
        ),
    ]
