from django.contrib import admin
from milhas.models import Cupom, Msg
from django.utils import timezone
from django.forms import TextInput, Textarea
from django.db import models
#from settings import MEDIA_URL

#from filtrate.filters import DateRangeFilter
#from daterange_filter.filter import DateTimeRangeFilter



class CupomAdmin(admin.ModelAdmin):
	
	list_display = ['id' , 'title', 'subtitle', 'cupom_start_date', 'cupom_end_date', 'code_cupom', 'status', 'sold_out', 'max_oferta', 'published']
	list_editable =  ['cupom_start_date', 'cupom_end_date', 'sold_out', 'max_oferta']
	list_filter = (
		'sold_out', 'max_oferta'
	)
	search_fields = ['title', 'subtitle', 'code_cupom']
	formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 40,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }
    
    


class MsgAdmin(admin.ModelAdmin):
	"""docstring for MsgAdmin"""
	list_display = ['message']

    

admin.site.register(Cupom,CupomAdmin)
admin.site.register(Msg, MsgAdmin)


