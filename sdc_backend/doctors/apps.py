from django.apps import AppConfig


class DoctorsConfig(AppConfig):
    name = 'doctors'

    def ready(self): #method just to import the signals
    	import doctors.signals