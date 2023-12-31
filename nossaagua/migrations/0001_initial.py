# Generated by Django 4.2.6 on 2023-10-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaltouAgua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostafalta', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Sim', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=11)),
                ('rua', models.CharField(max_length=30)),
                ('numero_casa', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=40)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
    ]
