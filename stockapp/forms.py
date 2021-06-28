from django.forms import ModelForm
from stockapp.models import StockList

class StockForm(ModelForm):
    class Meta:
        model = StockList
        fields = ['name' , 'industry' , 'mcap' , 'slug' , 'videourl' , 'description']