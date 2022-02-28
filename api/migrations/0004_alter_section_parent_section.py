# Generated by Django 4.0.2 on 2022-02-28 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_updated_at_section_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='parent_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.section'),
        ),
    ]