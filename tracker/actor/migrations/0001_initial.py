# Generated by Django 2.0 on 2018-01-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('actor_type', models.CharField(choices=[('author', 'Author'), ('editor', 'Editor'), ('publisher', 'Publisher'), ('printer', 'Printer'), ('thirdparty', 'Third party')], max_length=10)),
                ('pseudonym', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('group_type', models.CharField(choices=[('authors', 'Authors'), ('contributors', 'Contributors'), ('organization', 'Organization')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='groups',
            field=models.ManyToManyField(blank=True, to='actor.Group'),
        ),
    ]
