from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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
    "dec":"learn Django everyday",
}

def month_challenges(request, month):
    try:
        month_text = month_challenge[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound("Month is not valid")

