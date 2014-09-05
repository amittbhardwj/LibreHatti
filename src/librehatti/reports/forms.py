from django import forms

from search_choices import CLIENT_FIELD_CHOICES
from search_choices import CLIENT_ORDER_CHOICES
from search_choices import CONSTRAINT_CHOICES
import datetime
from django.forms.extras.widgets import SelectDateWidget

"""
displays checkboxes for Client Search
"""
class ClientForm(forms.Form):
    client_fields = forms.MultipleChoiceField(required=False,
    widget=forms.CheckboxSelectMultiple, choices=CLIENT_FIELD_CHOICES)


"""
displays chechboxes for Order Search
"""
class OrderForm(forms.Form):
    order = forms.MultipleChoiceField(required=False,
    widget=forms.CheckboxSelectMultiple, choices=CLIENT_ORDER_CHOICES)

"""
displays checkboxes for Constraints
"""
class AddConstraints(forms.Form):
    start_date = forms.DateField(required=False, initial='2014-01-01')
    end_date = forms.DateField(required=False, initial= datetime.date.today())
    month = forms.DateField(required=False, widget=SelectDateWidget)
    year = forms.DateField(required=False, widget=SelectDateWidget)
    name = forms.CharField(required=False)
    paid_service_tax = forms.IntegerField(required=False)
    paid_education_tax = forms.IntegerField(required=False)
    amount_given = forms.IntegerField(required=False)
    material = forms.CharField(required=False)
    type = forms.CharField(required=False)
    lab = forms.CharField(required=False)
    additional_constraints = forms.MultipleChoiceField(required=False,
    widget=forms.CheckboxSelectMultiple, choices= CONSTRAINT_CHOICES)
    