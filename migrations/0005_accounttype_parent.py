# Generated by Django 3.0.3 on 2020-03-05 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbaccounting', '0004_auto_20200305_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttype',
            name='parent',
            field=models.ForeignKey(help_text='Is this a subcategory (e.g. Current Assets)', null=True, on_delete=django.db.models.deletion.CASCADE, to='dbaccounting.AccountType'),
        ),
    ]