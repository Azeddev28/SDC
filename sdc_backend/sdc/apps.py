from django.apps import AppConfig


class SdcConfig(AppConfig):
    name = 'sdc'

    def ready(self): #method just to import the signals
    	import sdc.signals