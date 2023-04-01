# Generated by Django 4.1.7 on 2023-04-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('A', 'Intermediário'), ('S', 'Avançado')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('M', 'Manhã'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]
