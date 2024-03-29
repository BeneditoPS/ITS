# Generated by Django 4.2.2 on 2023-10-09 13:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='nota',
            field=models.TextField(default='Nenhuma', max_length=200),
        ),
        migrations.AlterField(
            model_name='declaracao',
            name='nota',
            field=models.TextField(default='Nenhuma', max_length=200),
        ),
        migrations.AlterField(
            model_name='peticao',
            name='nota',
            field=models.TextField(default='Nenhuma', max_length=200),
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utente', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('ano', models.CharField(max_length=50)),
                ('nota', models.TextField(default='Nenhuma', max_length=200)),
                ('estado', models.CharField(choices=[('Busca', 'Busca'), ('Pendente', 'Pendente'), ('Digitalizado', 'Digitalizado'), ('Assinatura', 'Assinatura'), ('Pronto a Levantar', 'Pronto a Levantar'), ('Concluido', 'Concluido')], default='Busca', max_length=50)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
