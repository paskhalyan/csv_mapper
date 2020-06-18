import csv
import io

from django.core.cache import cache
from django.shortcuts import render, redirect
from django.views import View

from .models import CSVMap
from .forms import UploadCSVForm, ChoicesForm

MODEL_FIELDS = [field.attname for field in CSVMap._meta.get_fields() if field.attname != 'id']


class UploadCSVView(View):
    def get(self, request):
        qs = CSVMap.objects.all()
        form = UploadCSVForm()

        return render(request, 'csv_mapper/index.html', {'form': form, 'objects': qs})

    def post(self, request):
        file_form = UploadCSVForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')))
            request.session['csv-data'] = list(reader)
            # cache.set('csv-fields', reader.fieldnames)
            choices_form = ChoicesForm()
            context = {'form': choices_form}

            return render(request, 'csv_mapper/field_choices.html', context)


def process_csv(request):
    csv_data = request.session['csv-data']
    object_list = []
    for item in csv_data:
        temp = {}
        for field in MODEL_FIELDS:
            temp[field] = item[request.POST[field]]
        obj = CSVMap(**temp)
        object_list.append(obj)
    CSVMap.objects.bulk_create(object_list)

    return redirect('home')
