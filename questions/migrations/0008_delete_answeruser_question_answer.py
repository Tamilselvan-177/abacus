# Generated by Django 4.1.13 on 2024-12-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_test_test_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerUser',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=''),
        ),
    ]
