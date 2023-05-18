# Generated by Django 2.1.1 on 2023-05-18 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=255)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('pay', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ofuserId', models.IntegerField()),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
                ('serviceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiredApp.Service')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=50)),
                ('creditcard', models.IntegerField()),
                ('role', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('taskId', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='touseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiredApp.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='ofuserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofuserId_Message_User', to='HiredApp.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='touseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touseId_Message_User', to='HiredApp.User'),
        ),
        migrations.AddField(
            model_name='contract',
            name='ofuserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofuserId_Contract_User', to='HiredApp.User'),
        ),
        migrations.AddField(
            model_name='contract',
            name='taskId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiredApp.Task'),
        ),
        migrations.AddField(
            model_name='contract',
            name='touseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touseId_Contract_User', to='HiredApp.User'),
        ),
        migrations.AddField(
            model_name='account',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiredApp.User'),
        ),
    ]
