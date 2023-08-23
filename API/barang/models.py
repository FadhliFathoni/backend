from django.db import models

class BarangModel(models.Model):
    nama_barang = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)