# Generated by Django 2.0.4 on 2018-05-01 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120, verbose_name='descrição')),
                ('numbers', models.PositiveIntegerField(verbose_name='números')),
                ('number_initial', models.IntegerField(default=0, verbose_name='número inicial')),
            ],
            options={
                'verbose_name': 'rifa',
                'verbose_name_plural': 'rifas',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='número')),
                ('booking_date', models.DateField(null=True, verbose_name='data da reserva')),
                ('is_paid', models.BooleanField(default=False, verbose_name='pago?')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Client', verbose_name='cliente')),
                ('raffle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Raffle', verbose_name='rifa')),
            ],
        ),
    ]
