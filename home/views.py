from django.shortcuts import render, redirect
# Create your views here.
import time

from django.http import HttpResponse
from .task import *


def home(request):
    send_email.delay()
    return HttpResponse("Hello from celery")