from django.shortcuts import render

from luz.conta.models import Conta


def graph(request, slug):

    bills = list(Conta.objects.all().order_by('date'))

    ctx = {'date': [bill.date.strftime("%m/%Y") for bill in bills],
           'amount_paid': [str(bill.amount_paid) for bill in bills],
           'mw': [bill.mw for bill in bills],
           'view_name': 'graph'
           }

    return render(request, f'{slug}/graph.html', context=ctx)
