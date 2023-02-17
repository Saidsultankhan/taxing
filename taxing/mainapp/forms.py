from django import forms
from mainapp.models import Company, Count, Types, Taxes, Months, Year
from users.models import CustomUser


class CompanyAddForm(forms.ModelForm):
    # type = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, to_field_name="type_of_company")

    class Meta:
        model = Company
        fields = ['name', 'type_of_company']
        exclude = ('owner', )
        widgets = {
            'summs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму оборота'
            }),
        }


class CountingForm(forms.ModelForm):

    class Meta:
        model = Count
        fields = ['summs',]
        widgets = {
            'summs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму оборота'
            })
        }


class TaxAddForm(forms.ModelForm):
    months = Months.objects.all()
    Месяц = forms.ModelChoiceField(queryset=months, to_field_name="name")

    class Meta:
        model = Taxes
        fields = ['tax', 'year',]
        exclude = ('company',)
        widgets = {
            'tax': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму оборота'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год'
            }),
        }

        # payday = 25
        # pay_month = form.cleaned_data.get('month')
        #
        # day = old_form.time.day
        # month = old_form.time.month
        # year = old_form.time.year
        # thirty_one = [1, 3, 5, 7, 8, 10, 12]
        # february = 2
        # thirty = [4, 6, 9, 11]
        # day_result = 0
        #
        # if pay_month == month or pay_month == 1 + month and day <= payday:
        #     tax = int(taxss) * (tax_sum / 100)
        #     old_form.tax = tax
        #     old_form.save(update_fields=['tax'])
        # else:
        #     if month in thirty_one:
        #         day_result = day - payday + 31
        #     elif month in thirty:
        #         day_result = day - payday + 30
        #     elif month == february:
        #         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        #             day_result = day - payday + 29
        #         else:
        #             day_result = day - payday + 28
        #     tax = int(taxss) * (tax_sum / 100)
        #     is_paid = tax * 0.033 * day_result
        #     old_form.tax = tax + not_paid
        #     old_form.save(update_fields=['tax'])
        #
        #     company.not_paid.add(is_paid)
        #     context = {
        #         'tax': tax,
        #         'taxss': taxss,
        #         'company': company,
        #         'not_paid': is_paid,
        #         'month': month
        #     }