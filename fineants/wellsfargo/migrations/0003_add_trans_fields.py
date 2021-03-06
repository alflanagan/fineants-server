# Generated by Django 3.2.4 on 2021-06-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0002_add_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='wellsfargostmttrans',
            name='labels',
            field=models.CharField(default='', help_text='rarely-used extra field', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wellsfargostmttrans',
            name='notes',
            field=models.CharField(default='', help_text='Notes about transaction from bank', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wellsfargostmttrans',
            name='original_description',
            field=models.CharField(blank=True, help_text='Raw description text sent by other party', max_length=500),
        ),
        migrations.AddField(
            model_name='wellsfargostmttrans',
            name='uniq_id',
            field=models.CharField(blank=True, help_text='not provided by bank but created by us', max_length=128, verbose_name='Unique ID'),
        ),
    ]
