from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Percent(models.Model):
    NUMBERS = (
        (4, 'ИП'),
        (6, 'OOO'),
        (15, 'НДС'),
    )
    percent_id = models.AutoField(primary_key=True)
    amount = models.PositiveSmallIntegerField(choices=NUMBERS)
    name = models.CharField(max_length=10, verbose_name='Название процента')

    class Meta:
        ordering = ['amount']
        verbose_name = 'Процент'
        verbose_name_plural = 'Проценты'

    def __str__(self):
        return '{}'.format(self.name)


class Types(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Percent, verbose_name='Название', on_delete=models.CASCADE, related_name='percents')

    class Meta:
        ordering = ['name']
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'

    def __str__(self):
        return '{}'.format(self.name)


class Months(models.Model):
    NAMES_OF_MONTHS = (
        ('1', 'Январь'),
        ('2', 'Февраль'),
        ('3', 'Март'),
        ('4', 'Апрель'),
        ('5', 'Май'),
        ('6', 'Июнь'),
        ('7', 'Июль'),
        ('8', 'Август'),
        ('9', 'Сентябрь'),
        ('10', 'Октябрь'),
        ('11', 'Ноябрь'),
        ('12', 'Декабрь'),
    )
    name = models.CharField(max_length=2, choices=NAMES_OF_MONTHS, verbose_name='Месяц')

    class Meta:
        ordering = ['name']
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'

    def __str__(self):
        return self.name


class Fines(models.Model):
    fine_id = models.AutoField(primary_key=True)
    summ = models.PositiveIntegerField(verbose_name='Сумма штрафа')

    def __str__(self):
        return '{}'.format(self.summ)

    class Meta:
        ordering = ['summ']
        verbose_name = 'Штраф'
        verbose_name_plural = 'Штраф'

#
# class Areas(models.Model):
#     NAMES_OF_MONTHS = (
#         ('1', 'Андижан'),
#         ('2', 'Бухара'),
#         ('3', 'город Ташкент'),
#         ('4', 'Джизак'),
#         ('5', 'Кашкадарья'),
#         ('6', 'Навои'),
#         ('7', 'Наманган'),
#         ('8', 'Республика Каракалпакстан'),
#         ('9', 'Самарканд'),
#         ('10', 'Сырдарьинская'),
#         ('11', 'Сурхандарья'),
#         ('12', 'Ташкентская область'),
#         ('13', 'Фергана'),
#         ('14', 'Хорезм'),
#     )
#     name = models.CharField(max_length=2, choices=NAMES_OF_MONTHS, verbose_name='Прописка')
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Прописка'
#         verbose_name_plural = 'Прописки'
#
#     def __str__(self):
#         return self.name


class Company(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Название компании')
    created = models.DateTimeField(verbose_name='Дата открытия компании', auto_now_add=True)
    type_of_company = models.ForeignKey(Types, verbose_name='Тип Юр.Лица', on_delete=models.CASCADE, related_name='types')
    not_paid = models.PositiveIntegerField(verbose_name='Штраф?', default=0)
    # area = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='Прописка')
    has_fine = models.BooleanField(verbose_name='Есть штраф?', default=False)
    paid_before = models.BooleanField(verbose_name='Все оплачено?', default=False)
    for_militiary = models.BooleanField(verbose_name='Для МВД?', default=False)
    # checked = models.BooleanField(verbose_name='Данные проверены', default=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:company_detail', kwargs={'pk': self.pk})


class Year(models.Model):
    year = models.PositiveSmallIntegerField(verbose_name='Год', unique=True, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.year)

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class Taxes(models.Model):
    month = models.ManyToManyField(Months, verbose_name='Месяцы', related_name='months')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    company = models.ManyToManyField(Company, verbose_name='Компания', related_name='companies')
    tax = models.IntegerField(verbose_name='Сумма оборота', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    # is_paid = models.BooleanField(verbose_name='Налог оплачен')

    class Meta:
        ordering = ['time']
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return '{}'.format(self.tax)

    def get_absolute_url(self):
        return reverse('mainapp:tax_detail', kwargs={'pk': self.pk})


class Payment(models.Model):
    quarters = {
        ('1-ый квартал', '1'),
        ('2-ой квартал', '2'),
        ('3-ий квартал', '3'),
        ('4-ый квартал', '4'),
    }
    amount = models.OneToOneField(Taxes, on_delete=models.CASCADE, verbose_name='Количество')
    month = models.OneToOneField(Months, on_delete=models.CASCADE, verbose_name='Месяц')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, verbose_name='Компания')
    year = models.OneToOneField(Year, on_delete=models.CASCADE, max_length=10, blank=True, verbose_name='Год')
    sqrt = models.CharField(max_length=15, verbose_name='Название квартала', choices=quarters)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return self.sqrt


class Count(models.Model):
    summs = models.IntegerField(verbose_name='Сумма для подсчета')

    class Meta:
        verbose_name = 'Подсчет'
        verbose_name_plural = 'Подсчеты'