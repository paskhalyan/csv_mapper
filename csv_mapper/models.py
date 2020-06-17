from django.db import models


class CSVMap(models.Model):
    id_in_doc = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    app_name = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
