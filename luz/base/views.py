from datetime import date

from django.shortcuts import render


data = {'date': [date(2020, 1, 1), date(2020, 2, 1), date(2020, 3, 1), date(2020, 4, 1), date(2020, 5, 1)],
        'MW': [300, 455, 456, 80, 608]
        }


# Create your views here.
def home(request):
    ctx = {'date': [date.strftime("%d/%m/%Y") for date in data['date']],
           'MW':  data['MW']
           }
    return render(request, "base/grafico.html", context=ctx)
