# Generated by Django 4.2.4 on 2023-08-17 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='application.post', verbose_name='Посты блога'),
        ),
    ]
