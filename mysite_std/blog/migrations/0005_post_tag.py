# Generated by Django 4.1 on 2022-11-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="tag", field=models.ManyToManyField(to="blog.tag"),
        ),
    ]
