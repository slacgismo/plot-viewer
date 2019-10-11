from django import forms
from .models import plot



class SortForm(forms.Form):

    x_axis_search = forms.ModelChoiceField(queryset=plot.objects.all())
    y_axis_search = forms.ModelChoiceField(queryset=plot.objects.all())

    # x_axis_search = forms.ChoiceField(choices = (('hardCover', 'Hard Cover'), ('looseLeaf', 'Loose Leaf'), ('paperBack', 'Paper Back'), ('pdf', 'PDF')))
    # y_axis_search = forms.ChoiceField(choices = (('hardCover', 'Hard Cover'), ('looseLeaf', 'Loose Leaf'), ('paperBack', 'Paper Back'), ('pdf', 'PDF')))
    #
    # NORMALIZATION_CHOICES = (
    #     ('summer_tatal_peak_normalization', 'summer_tatal_peak_normalization'),
    #     ('hourly_normalization', 'hourly_normalization'),
    # )
    #
    #
    #
    #
    #
    #
    # # x_axis_search = forms.ChoiceField(choices= (('season', 'season'),('mix_type', 'mix_type'),('location'), ('location')))
    # y_axis_search = forms.ChoiceField(required=True, label="y-axis", widget=forms.Select(choices=SORT_CHOICES))
    # normalization = forms.ChoiceField(required=True, label="normalization", widget=forms.Select(choices=NORMALIZATION_CHOICES))
