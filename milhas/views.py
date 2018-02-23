from django.shortcuts import render
from milhas.models import Cupom, Msg
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.db import close_old_connections
close_old_connections()

def get_countdown(results, cupons, max_oferta):
    last_cupom = cupons.order_by('-cupom_end_date').first()
    last_maxoferta = max_oferta.order_by('-cupom_end_date').last()
    return last_cupom if last_cupom else last_maxoferta

def home(request):
	#import ipdb; ipdb.set_trace()

	today = datetime.now()

	#results = Cupom.objects.filter(cupom_start_date__lte=today, cupom_end_date__gte=today)

	results = Cupom.objects.all()
	message = Msg.objects.all()
	message = message.first()
	results_sold_out = results.filter(cupom_end_date__lt=today)
	cupons = results.filter(max_oferta=0, cupom_start_date__lte=today, cupom_end_date__gt=today)
	max_oferta = results.filter(max_oferta=1,cupom_start_date__lte=today, cupom_end_date__gt=today)
	max_oferta_sold_out = results.filter(max_oferta=1,cupom_end_date__lt=today)

	return render(request, 'home.html', context={
		"cupons": cupons,
		"message": message,
		"sold_out": results_sold_out.order_by('-cupom_end_date') if results_sold_out else None,
		"countdown": get_countdown(results, cupons, max_oferta),
		"max_oferta": max_oferta.order_by('-cupom_end_date') if max_oferta else None,
		"max_oferta_sold_out": max_oferta_sold_out.order_by('-cupom_end_date') if max_oferta_sold_out else None,
		"request": request
	})
def how(request):
	return render(request, 'how.html')
