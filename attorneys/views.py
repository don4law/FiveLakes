# Attorneys Views
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required

def attorney_view(request):
  context = {'title': 'Attorneys'}
  return render(request, 'templates/attorneys.html',context)
