from django.contrib import admin
from django.urls import path

from .views import process_csv, UploadCSVView # upload_csv_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UploadCSVView.as_view(), name='home'),
    path('process-csv', process_csv, name='process_csv'),
]
