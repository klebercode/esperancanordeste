# coding: utf-8
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# from forms import *

def home(request):
    context = {}

    return render(request, 'index.html', context)
