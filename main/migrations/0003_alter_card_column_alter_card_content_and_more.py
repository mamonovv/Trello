# Generated by Django 4.0 on 2022-01-09 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_column_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='column',
            field=models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, to='main.column', verbose_name='В какой колонке'),
        ),
        migrations.AlterField(
            model_name='card',
            name='content',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='card',
            name='deadline',
            field=models.DateTimeField(null=True, verbose_name='Срок выполнения'),
        ),
        migrations.AlterField(
            model_name='card',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/', verbose_name='Фото'),
        ),
    ]
