# Generated by Django 4.0.2 on 2022-02-26 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_titile_section_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='updated_at',
            new_name='last_updated',
        ),
    ]