# Generated by Django 4.2.5 on 2023-10-04 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mine_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minecode', models.CharField(max_length=12)),
                ('minename', models.CharField(max_length=100)),
                ('ownercode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='acc_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minename', models.CharField(max_length=100)),
                ('acc_date', models.DateTimeField(verbose_name='Accident Date')),
                ('killed', models.IntegerField(default=0)),
                ('injured', models.IntegerField(default=0)),
                ('coscode', models.CharField(max_length=4)),
                ('minecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aentry.mine_details')),
            ],
        ),
    ]
