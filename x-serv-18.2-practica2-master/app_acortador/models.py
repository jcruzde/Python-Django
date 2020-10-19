from django.db import models

# Create your models here.
class URL(models.Model):
    URL_larga = models.CharField(max_length=32)

    # Para que en el admin veamos el nombre de la URL
    def __str__(self):
        URL_larga = self.URL_larga
        return URL_larga

    '''
    ID (Primary Key) => localhost:8000/ID => URL acortada
    URL_larga => Url completa
    '''
