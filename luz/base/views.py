from django.shortcuts import render


def home(request):
    ctx = {'view_name': 'home'}
    return render(request, "base/home.html", context=ctx)
