# Generated by Django 3.1.1 on 2022-04-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0008_auto_20220420_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='brand',
        ),
        migrations.AddField(
            model_name='request',
            name='tags',
            field=models.CharField(choices=[('Perishable', 'Perishable'), ('Non-perishable', 'Non-perishable'), ('Health', 'Health')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]