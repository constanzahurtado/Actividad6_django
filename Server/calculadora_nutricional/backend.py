from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import Registro

class MyBackend(BaseBackend):
    def authenticate(self, request, username = None , password = None):
        try:
            proveedor = Registro.objects.filter(rut=username, password = password).get()
            return proveedor
        except:
            return None

    def get_user(self, rut):
        try:
            return Registro.objects.get(pk = rut)
        except Registro.DoesNotExist:
            return None