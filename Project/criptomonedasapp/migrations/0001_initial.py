# Generated by Django 2.1.7 on 2019-04-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criptomoneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('market_cap', models.IntegerField(default='')),
                ('price', models.IntegerField(default='')),
                ('volume_24h', models.IntegerField(default='')),
                ('change_24h', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(default='', max_length=32)),
                ('cuerpo', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
