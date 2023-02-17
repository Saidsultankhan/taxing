from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from mainapp.models import Company, Taxes, Payment, Types, Percent, Months
from users.models import CustomUser
from mainapp.forms import CompanyAddForm, CountingForm, TaxAddForm
from bs4 import BeautifulSoup as bf
import requests as req
import datetime


class UserView(View):
    model = Company
    template_name = 'mainpage.html'
    context_object_name = 'company'

    def get(self, request):
        a = Company.objects.values()
        b = Company
        context = {
            'tax': a
        }
        return render(request, self.template_name, context=context)


class StatsView(DetailView):
    model = Company
    template_name = 'account.html'
    context_object_name = 'company'
    urls = 'https://bank.uz/currency'
    site_url = req.get(urls)
    soup = bf(site_url.text, "html.parser")
    price = soup.findAll('div', class_='tabs-a')
    list_for_current_summ_of_dollar = []

    for i in price[0]:
        # print(i)
        for u in i.text:
            # print(u)
            list_for_current_summ_of_dollar.append(u)
    # print(list_for_current_summ_of_dollar)
    dollar = list_for_current_summ_of_dollar[11:17]
    do = ''
    for i in dollar:
        if i != ' ':
            do += i
        str(i)
    print(dollar)
    print(do)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        taxes = Taxes.objects.filter(company=self.kwargs['pk'])
        taxes_2021 = Taxes.objects.filter(year=2021)
        taxes_2022 = Taxes.objects.filter(year=2022)
        context['taxs'] = taxes

        first_sqrt_2021 = Taxes.objects.filter(year=2021)[:3]
        first_year_client = CustomUser.objects.get()[:3]
        f_r_2021 = 0
        for i in first_sqrt_2021:
            i = i.tax * 25
            f_r_2021 += i
        context['first_sqrt_2021'] = f_r_2021

        second_sqrt_2021 = Taxes.objects.filter(year=2021)[3:6]
        s_r_2021 = 0
        for i in second_sqrt_2021:
            i = i.tax * 25
            s_r_2021 += i
        context['second_sqrt_2021'] = s_r_2021

        third_sqrt_2021 = Taxes.objects.filter(year=2021)[6:9]
        t_r_2021 = 0
        for i in third_sqrt_2021:
            i = i.tax * 25
            t_r_2021 += i
        context['third_sqrt_2021'] = t_r_2021

        firth_sqrt_2021 = Taxes.objects.filter(year=2021)[9:12]
        th_r_2021 = 0
        for i in firth_sqrt_2021:
            i = i.tax * 25
            th_r_2021 += i
        context['firth_sqrt_2021'] = th_r_2021

        first_sqrt_2022 = Taxes.objects.filter(year=2022)[:3]
        f_r_2022 = 0
        for i in first_sqrt_2022:
            i = i.tax * 25
            f_r_2022 += i
        context['first_sqrt_2022'] = f_r_2022

        second_sqrt_2022 = Taxes.objects.filter(year=2022)[3:6]
        s_r_2022 = 0
        for i in second_sqrt_2022:
            i = i.tax * 25
            s_r_2022 += i
        context['second_sqrt_2022'] = s_r_2022

        third_sqrt_2022 = Taxes.objects.filter(year=2022)[6:9]
        t_r_2022 = 0
        for i in third_sqrt_2022:
            i = i.tax * 25
            t_r_2022 += i
        context['third_sqrt_2022'] = t_r_2022

        firth_sqrt_2022 = Taxes.objects.filter(year=2022)[9:12]
        fr_r_2022 = 0
        for i in firth_sqrt_2022:
            i = i.tax * 25
            f_r_2021 += i
        context['firth_sqrt_2022'] = fr_r_2022

        taxes_2021_list = []
        for i in taxes_2021:
            i = int(i.tax)
            tax = i * 25
            taxes_2021_list.append(tax)
        context['taxes_2021'] = taxes_2021_list

        taxes_2022_list = []
        for i in taxes_2022:
            i = int(i.tax)
            tax = i * 25
            taxes_2022_list.append(tax)
        context['taxes_2022'] = taxes_2022_list

        oborot = []
        tax_in_summ = 0
        usd_list = []
        dict_for_stats = {}
        if taxes:
            for tax in taxes:
                a = tax.tax
                int(a)
                tax_in_summ += a
                summ_of_oborot = a*25
                oborot.append(summ_of_oborot)
                oborot_2021 = taxes.filter()
                if oborot:
                    total = 0
                    usd_total = 0
                    for i in oborot:
                        total += i
                        context['total'] = total
                    usd = total / int(self.do)
                    usd_1 = float('{:.2f}'.format(usd))
                    usd_list.append(usd_1)
                    usd_total += usd_1
                    context['tax_in_dollar'] = usd_total

        context['taxes'] = tax_in_summ
        tax_in_dollar = tax_in_summ / int(self.do)
        dollar = float('{:.2f}'.format(tax_in_dollar))
        context['oborot'] = oborot
        context['usd'] = usd_list

        return context


def company_add(request):
    form = CompanyAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return redirect(request.user.get_absolute_url())
    else:
        form = CompanyAddForm()
        return render(request, template_name='company_add.html', context={'form': form})


# def tax_add(request):
#     if request.method == 'POST':
#         form = TaxAddForm(request.POST)
#         company = request.user.company
#         if form.is_valid():
#             tax = form.save()
#             tax.company.add(request.user.company)
#             return redirect(company.get_absolute_url())
#     else:
#         form = TaxAddForm()
#         return render(request, template_name='tax_add.html', context={'form': form})

def tax_add(request):
    if request.method == 'POST':
        company = Company.objects.get(id=request.user.company.pk)
        form = TaxAddForm(request.POST)
        tax_sum = int(request.user.company.type_of_company.name.amount)
        not_paid = company.not_paid
        has_fine = request.user.company.has_fine
        # tashkent = pytz.timezone('Asia/Tashkent')
        # current_tashkent_time = datetime.now(tashkent)
        # current_time = current_tashkent_time.day
        # current_a = current_tashkent_time.month
        # current_s = current_tashkent_time.year
        if form.is_valid():
            old_form = form.save()
            taxss = form.cleaned_data.get('tax')
            # company_time = form.cleaned_data.get('time')
            old_form.company.add(request.user.company)
            if not_paid > 0:
                tax = int(taxss) * (tax_sum / 100)
                old_form.tax = tax + not_paid
                company.not_paid = 0
                company.save()
                old_form.save(update_fields=['tax'])
            else:
                tax = int(taxss) * (tax_sum / 100)
                old_form.tax = tax
                old_form.save(update_fields=['tax'])

            context = {
                'tax': tax,
                'taxss': taxss,
                'company': company,
            }
        return render(request, template_name='tax_add.html', context=context)
    else:
        form = TaxAddForm()
        return render(request, template_name='tax_add.html', context={'form': form})


def count_view(request):
    if request.method == 'POST':
        form = CountingForm(request.POST)
        tax_sum = int(request.user.company.type_of_company.name.amount)
        if form.is_valid():
            form.save()
            summ = form.cleaned_data.get('summs')
            tax = int(summ) * (tax_sum/100)
            context = {
                'tax': tax,
                'sum': summ
            }
            return render(request, template_name='count.html', context=context)
    else:
        form = CountingForm()
    return render(request, 'count.html', {'form': form})


class TaxDetailView(DetailView):
    model = Taxes
    template_name = 'tax_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tax'] = Taxes.objects.get(pk=self.kwargs['pk'])


def latest_news(request):
    news = """
Снижение налоговой нагрузки для нерезидентов
Поправками снижается ставка НДФЛ по доходам нерезидентов из источников в Узбекистане (за исключением дивидендов, процентов и доходов от фрахта) с 20% до 12%.

Например, если доход нерезидента за месяц составлял 1000 долларов, то в бюджет уплачивалось 200 долларов от этой суммы. Сейчас сумма удержания составит 120 долларов.

Сниженная ставка применяется к доходам, начисленным с 1 мая 2022 года.

При этом, как отмечает Минфин, отчетность по НДФЛ за май-июнь можно не пересдавать. Так как отчет представляется нарастающим итогом с начала года, достаточно отразить корректировки по итогам июля.

С 1 апреля 2022 года по 31 декабря 2024 года доходы физических лиц (акционеров), являющихся резидентами и нерезидентами Узбекистана, в виде дивидендов по акциям освобождаются от НДФЛ. По доходам компаний-нерезидентов в виде дивидендов по принадлежащим им (акционерам) акциям применяется налоговая ставка по налогу на прибыль в размере 5%. Доходы физических и юрлиц — резидентов и нерезидентов в виде процентов по облигациям хозяйственных обществ освобождаются от НДФЛ и налога на прибыль.
"""
    context = {
        'news': news
    }
    return render(request, template_name='latest_news.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, template_name='contacts.html', context=context)
