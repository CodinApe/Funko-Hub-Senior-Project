# Generated by Django 4.2.5 on 2023-09-29 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0002_comment_post_post_category_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_hub.post'),
        ),
    ]
