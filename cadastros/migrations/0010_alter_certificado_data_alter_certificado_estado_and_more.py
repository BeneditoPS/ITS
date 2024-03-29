# Generated by Django 4.2.2 on 2023-12-10 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_alter_levantamento_certificado_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 653347), verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='estado',
            field=models.CharField(choices=[('Busca', 'Busca'), ('Pendente', 'Pendente'), ('Por Digitalizar', 'Por Digitalizar'), ('Digitalizado', 'Digitalizado'), ('Assinatura', 'Assinatura'), ('Pronto a Levantar', 'Pronto a Levantar'), ('Concluido', 'Concluido')], default='Busca', max_length=50),
        ),
        migrations.AlterField(
            model_name='declaracao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 654345), verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='declaracao',
            name='estado',
            field=models.CharField(choices=[('Busca', 'Busca'), ('Pendente', 'Pendente'), ('Por Digitalizar', 'Por Digitalizar'), ('Digitalizado', 'Digitalizado'), ('Assinatura', 'Assinatura'), ('Pronto a Levantar', 'Pronto a Levantar'), ('Concluido', 'Concluido')], default='Busca', max_length=50),
        ),
        migrations.AlterField(
            model_name='historico',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 656344), verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='historico',
            name='estado',
            field=models.CharField(choices=[('Busca', 'Busca'), ('Pendente', 'Pendente'), ('Por Digitalizar', 'Por Digitalizar'), ('Digitalizado', 'Digitalizado'), ('Assinatura', 'Assinatura'), ('Pronto a Levantar', 'Pronto a Levantar'), ('Concluido', 'Concluido')], default='Busca', max_length=50),
        ),
        migrations.AlterField(
            model_name='levantamento_certificado',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 657345), verbose_name='Data de Levantamento'),
        ),
        migrations.AlterField(
            model_name='levantamento_declaracao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 658342), verbose_name='Data de Levantamento'),
        ),
        migrations.AlterField(
            model_name='levantamento_declaracao',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='levantamento_historico',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 658342), verbose_name='Data de Levantamento'),
        ),
        migrations.AlterField(
            model_name='levantamento_historico',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='peticao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 20, 42, 32, 655346), verbose_name='Data de Entrada'),
        ),
    ]
