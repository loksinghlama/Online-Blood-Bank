# Generated by Django 2.2.4 on 2019-08-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_request', models.CharField(max_length=40)),
                ('mobile_request', models.IntegerField()),
                ('address_request', models.CharField(max_length=100)),
                ('email_request', models.CharField(max_length=30)),
                ('bloodgroup_request', models.CharField(max_length=5)),
                ('dateline_request', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='stockinput',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
