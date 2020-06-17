import csv
import io

from django.shortcuts import render, redirect
from django.views import View

from .models import CSVMap
from .forms import UploadCSVForm

MODEL_FIELDS = [field.attname for field in CSVMap._meta.get_fields() if field.attname != 'id']


class UploadCSVView(View):
    def get(self, request):
        qs = CSVMap.objects.all()
        form = UploadCSVForm()

        return render(request, 'csv_mapper/index.html', {'form': form, 'objects': qs})

    def post(self, request):
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')))
            request.session['csv-data'] = list(reader)

            context = {
                'csv_fields': reader.fieldnames,
                'model_fields': MODEL_FIELDS
            }

            return render(request, 'csv_mapper/field_choices.html', context)


def process_csv(request):
    csv_data = request.session['csv-data']
    object_list = []
    for item in csv_data:
        temp = {}
        for field in MODEL_FIELDS:
            temp[field] = item[request.GET[field]]
        obj = CSVMap(**temp)
        object_list.append(obj)
    CSVMap.objects.bulk_create(object_list)

    return redirect('home')
