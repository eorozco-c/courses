# Generated by Django 2.2.4 on 2021-08-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='app_curso.Course')),
            ],
        ),
    ]