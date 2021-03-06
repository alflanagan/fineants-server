# Generated by Django 3.2.3 on 2021-05-30 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=200)),
                ('bank', models.ForeignKey(help_text='Financial institution holding the account', on_delete=django.db.models.deletion.PROTECT, to='accounts.bank')),
            ],
            options={
                'unique_together': {('bank', 'account_number')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('to_from', models.CharField(max_length=100)),
                ('posted', models.DateTimeField()),
                ('memo', models.TextField()),
                ('is_debit', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.bankaccount')),
            ],
            options={
                'unique_together': {('account', 'posted')},
            },
        ),
    ]
