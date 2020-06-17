from django import forms

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
