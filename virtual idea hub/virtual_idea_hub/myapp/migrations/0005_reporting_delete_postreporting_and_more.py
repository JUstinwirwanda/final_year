# Generated by Django 5.0.2 on 2024-04-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_postawareness_postcomplain_postemergency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('report_description', models.TextField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='PostReporting',
        ),
        migrations.AddField(
            model_name='category',
            name='manager_email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
