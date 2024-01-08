# Generated by Django 4.2.2 on 2023-12-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_alter_levantamento_certificado_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levantamento_certificado',
            name='documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.certificado', unique=True),
        ),
    ]