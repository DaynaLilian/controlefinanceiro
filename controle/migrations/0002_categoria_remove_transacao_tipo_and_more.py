# Generated by Django 5.1.1 on 2024-11-04 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('REC', 'RECEITA'), ('DSP', 'DESPESA')], max_length=3)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.categoria'),
        ),
    ]
