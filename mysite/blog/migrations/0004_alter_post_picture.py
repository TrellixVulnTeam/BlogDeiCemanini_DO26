# Generated by Django 4.0.2 on 2022-02-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/post/% pk'),
        ),
    ]
