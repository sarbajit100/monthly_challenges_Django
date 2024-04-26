from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

month_challenge = {
    "jan":"Do not eat meat everyday",
    "feb":"Walk everyday 20 min",
    "mar":"learn Django everyday",
    "apr":"learn Django 20 min a day",
    "may":"Play 20 min A day outdoor",
    "jun":"drink 5 liter every day",
    "july":"Eat halthy meal everyday",
    "Agu":"Do not eat meat everyday",
    "sep":"learn Django everyday",
    "oct":"drink 5 liter every day",
    "nov":"learn Django 20 min a day",
    "dec":None,
}

def index(request):
    months = list(month_challenge.keys())

    return render (request, "challenges/index.html", {
        "months": months
    })

def month_challenges_by_number(request, month):
    months = list(month_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Not A Valid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_challenges(request, month):
    try:
        month_text = month_challenge[month]
        
        return render(request, "challenges/challenge.html", {
            "text":month_text,
            "month":month                                         
        })
    except:
        raise Http404()

