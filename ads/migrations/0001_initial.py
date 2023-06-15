# Generated by Django 4.2.2 on 2023-06-15 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=1000, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.categories')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
