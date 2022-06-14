# Generated by Django 4.0.4 on 2022-06-13 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subcomment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='blogapp.comment'),
            preserve_default=False,
        ),
    ]