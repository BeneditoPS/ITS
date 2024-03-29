# Generated by Django 4.2.2 on 2023-12-10 13:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0005_levantamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levantamento_Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utente', models.CharField(max_length=200, verbose_name='Nome do Utente')),
                ('data', models.DateField(default=datetime.datetime.now, verbose_name='Data de Levantamento')),
                ('parentesco', models.CharField(choices=[('Proprietário]', 'Proprietário'), ('Pai', 'Pai'), ('Mãe', 'Mãe'), ('Irmão(ã)', 'Irmão(ã)'), ('Tio(a)', 'Tio(a)'), ('Amigo', 'Amigo'), ('Outros', 'Outros')], max_length=50, verbose_name='Grau de Parentesco')),
                ('nota', models.TextField(default='Nenhuma', max_length=200)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.certificado', unique=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Levantamento_Declaracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utente', models.CharField(max_length=200, verbose_name='Nome do Utente')),
                ('data', models.DateField(default=datetime.datetime.now, verbose_name='Data de Levantamento')),
                ('parentesco', models.CharField(choices=[('Proprietário]', 'Proprietário'), ('Pai', 'Pai'), ('Mãe', 'Mãe'), ('Irmão(ã)', 'Irmão(ã)'), ('Tio(a)', 'Tio(a)'), ('Amigo', 'Amigo'), ('Outros', 'Outros')], max_length=50, verbose_name='Grau de Parentesco')),
                ('nota', models.TextField(default='Nenhuma', max_length=200)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.certificado', unique=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Levantamento_Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utente', models.CharField(max_length=200, verbose_name='Nome do Utente')),
                ('data', models.DateField(default=datetime.datetime.now, verbose_name='Data de Levantamento')),
                ('parentesco', models.CharField(choices=[('Proprietário]', 'Proprietário'), ('Pai', 'Pai'), ('Mãe', 'Mãe'), ('Irmão(ã)', 'Irmão(ã)'), ('Tio(a)', 'Tio(a)'), ('Amigo', 'Amigo'), ('Outros', 'Outros')], max_length=50, verbose_name='Grau de Parentesco')),
                ('nota', models.TextField(default='Nenhuma', max_length=200)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.certificado', unique=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Levantamento',
        ),
    ]
