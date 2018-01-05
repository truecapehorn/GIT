from django import forms

from .models import Row

class RowForm(forms.ModelForm):

    class Meta:
        model = Row
        fields = ('state',
                  'investor',
                  'contract_number',
                  'zip_code',
                  'manager',
                  'invoice',
                  'design',
                  'rcd_date',
                  'implementation_date',
                  'doer',
                  'comments',
                  'coutry',


                  )


class SearchForm(forms.Form):
        STATUS_CHOICES = (('investor', 'Inwestor'),
                          ('contract_number', 'Nr kontraktu'),
                          ('zip_code', 'Kod pocztowy'),
                          ('manager', 'Kierownik'),
                          ('design', 'Projektant'),
                          ('implementation_date', 'Data wykonania'),
                          ('coutry', 'Kraj'),


                          )
        col=forms.ChoiceField(label='Kolumna',choices=STATUS_CHOICES,)
        query = forms.CharField(label='Pytanie', max_length=100)
