# coding: utf-8

from django.db import models
import pytz
from datetime import datetime
from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

# Create your models here.
class Cupom(models.Model):
	title = models.TextField(max_length=20, verbose_name='Título',default='título')
	subtitle = models.TextField(default='subtitulo',max_length=40, verbose_name='Para')
	status =  models.TextField(default='Últimas Passagens', max_length=20, verbose_name='Estado')
	sold_out = models.BooleanField(default=1,verbose_name='Esgotado')
	max_oferta = models.BooleanField(default=1)
	#quantity = models.PositiveIntegerField(verbose_name='Quantidade')
	code_cupom = models.CharField(max_length=20, unique=True,verbose_name='Código do Cupom')
	cupom_start_date = models.DateTimeField(null=True, blank=False,verbose_name='Data Início Cupom',)
	cupom_end_date =  models.DateTimeField(null=True, blank=False, verbose_name='Data Fim Cupom')
	date_create = models.DateTimeField(auto_now_add=True)
	date_alteration = models.DateTimeField(auto_now=True)
	



	def published(self):
		#print(self.cupom_start_date, datetime.now(), self.cupom_end_date)
		return self.cupom_start_date < datetime.now() < self.cupom_end_date
	published.boolean = True
	published.short_description = "Publicado?"


	class Meta:
		verbose_name = "Cupom"
		verbose_name_plural = "Cupons"

	def __str__(self):
		return self.title[:50]

class Msg(models.Model):
	message = models.TextField(max_length=200, verbose_name='Mensagem',default='Mensagem...')
	def __str__(self):
		return self.message[:200]




