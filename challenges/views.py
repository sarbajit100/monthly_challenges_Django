from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "dec":"learn Django everyday",
}

def index(request,):
    list_items = ""
    months = list(month_challenge.keys())
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenges", args=[month])
        list_items += f"<h1><li><a href=\"{month_path}\">{capitalize_month}</a></li></h1>"
        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def month_challenges_by_number(request, month):
    months = list(month_challenge.keys())
    if month > len(months):
        return HttpResponse("Not A Valid Month")
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
        return HttpResponseNotFound("Month is not valid")

