from django import forms
from django.core.cache import cache

from .models import CSVMap

MODEL_FIELDS = CSVMap._meta.fields


class UploadCSVForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.clean().get('file')
        filename = file.name
        if not filename.endswith('.csv'):
            raise forms.ValidationError('File is not a CSV. Please upload only CSV files!')

        return file


class ChoicesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        self.fields['id_in_doc'] = forms.ChoiceField(choices=get_choices())
        self.fields['first_name'] = forms.ChoiceField(choices=get_choices())
        self.fields['last_name'] = forms.ChoiceField(choices=get_choices())
        self.fields['email'] = forms.ChoiceField(choices=get_choices())
        self.fields['gender'] = forms.ChoiceField(choices=get_choices())
        self.fields['ip_address'] = forms.ChoiceField(choices=get_choices())
        self.fields['app_name'] = forms.ChoiceField(choices=get_choices())

        def clean(self):
            """Fields validation should be implemented later"""
            pass


def get_choices():
    # choices = cache.get('csv-fields')
    # cache.delete('csv-fields')
    # choices = ((choice, choice) for choice in choices)
    choices = (
        ('id', 'id'),
        ('first_name', 'first_name'),
        ('last_name', 'last_name'),
        ('email', 'email'),
        ('gender', 'gender'),
        ('ip_address', 'ip_address'),
        ('app_name', 'app_name'),
    )

    return choices

