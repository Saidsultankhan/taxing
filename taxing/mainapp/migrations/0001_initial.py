# Generated by Django 4.0.5 on 2023-01-20 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата открытия компании')),
                ('not_paid', models.PositiveIntegerField(default=0, verbose_name='Штраф?')),
                ('has_fine', models.BooleanField(default=False, verbose_name='Есть штраф?')),
                ('paid_before', models.BooleanField(default=False, verbose_name='Все оплачено?')),
                ('for_militiary', models.BooleanField(default=False, verbose_name='Для МВД?')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summs', models.IntegerField(verbose_name='Сумма для подсчета')),
            ],
            options={
                'verbose_name': 'Подсчет',
                'verbose_name_plural': 'Подсчеты',
            },
        ),
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('fine_id', models.AutoField(primary_key=True, serialize=False)),
                ('summ', models.PositiveIntegerField(verbose_name='Сумма штрафа')),
            ],
            options={
                'verbose_name': 'Штраф',
                'verbose_name_plural': 'Штраф',
                'ordering': ['summ'],
            },
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Январь'), ('2', 'Февраль'), ('3', 'Март'), ('4', 'Апрель'), ('5', 'Май'), ('6', 'Июнь'), ('7', 'Июль'), ('8', 'Август'), ('9', 'Сентябрь'), ('10', 'Октябрь'), ('11', 'Ноябрь'), ('12', 'Декабрь')], max_length=2, verbose_name='Месяц')),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Percent',
            fields=[
                ('percent_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField(choices=[(4, 'ИП'), (6, 'OOO'), (15, 'НДС')])),
                ('name', models.CharField(max_length=10, verbose_name='Название процента')),
            ],
            options={
                'verbose_name': 'Процент',
                'verbose_name_plural': 'Проценты',
                'ordering': ['amount'],
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, unique=True, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Года',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='percents', to='mainapp.percent', verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Виды',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('tax', models.IntegerField(blank=True, null=True, verbose_name='Сумма оборота')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('company', models.ManyToManyField(related_name='companies', to='mainapp.company', verbose_name='Компания')),
                ('month', models.ManyToManyField(related_name='months', to='mainapp.months', verbose_name='Месяцы')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sqrt', models.CharField(choices=[('3-ий квартал', '3'), ('1-ый квартал', '1'), ('2-ой квартал', '2'), ('4-ый квартал', '4')], max_length=15, verbose_name='Название квартала')),
                ('amount', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.taxes', verbose_name='Количество')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.company', verbose_name='Компания')),
                ('month', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.months', verbose_name='Месяц')),
                ('year', models.OneToOneField(blank=True, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='mainapp.year', verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='type_of_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='mainapp.types', verbose_name='Тип Юр.Лица'),
        ),
    ]
