# Generated by Django 3.2.12 on 2022-03-02 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0004_delete_newspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedblogposts',
            name='related_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailpages.blogpage'),
        ),
    ]
