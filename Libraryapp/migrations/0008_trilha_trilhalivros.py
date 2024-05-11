# Generated by Django 4.1.7 on 2024-05-11 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Libraryapp', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trilha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrilhaLivros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('posicao_na_trilha', models.IntegerField()),
                ('book_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.book')),
                ('library_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.library')),
                ('trilha_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.trilha')),
            ],
        ),
    ]