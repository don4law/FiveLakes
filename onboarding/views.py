# Onboarding Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import date, datetime, timezone
from django.utils.dateparse import parse_datetime
from attorneys.models import Employee, Employee_More_Model
from onboarding.models import Onboarding_Detail_Model
from onboarding.forms import Onboarding_Form, Onboarding_Form2

@login_required(login_url=reverse_lazy('login'))
def onboarding_view(request):
    context = {'title': 'Onboarding'}
    # Get attorneys hired that have not yet completed onboarding
    onboarding_list = Employee.objects.filter(is_active=True, onboarding_complete=False)
    context.update({'onboarding_list': onboarding_list})
    return render(request, 'templates/onboarding.html', context)

@login_required(login_url=reverse_lazy('login'))
def onboarding_detail(request, pk=None):
    context = {'title': 'Onboarding'}
    employee = Employee.objects.get(employee_id=pk)
    context.update({'employee': employee})
    onboarding_checklist = Onboarding_Detail_Model.objects.get_or_create(employee_id_id=pk)
    if request.method == "POST":
        form = Onboarding_Form(request.POST, instance=onboarding_checklist[0])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.employee_id_id = pk
            if obj.send_pp_docs and obj.send_software_docs:
                employee.onboarding_step = "Schedule Training"
            elif obj.send_onboarding_email and (obj.puzzle_form or obj.return_ICA or obj.notify_Huron):
                employee.onboarding_step = "Send Onboarding / Training Docs"
            else:
                employee.onboarding_step = "Administrative Tasks"
            employee.save()
            obj.save()
            return HttpResponseRedirect(reverse_lazy('onboarding_detail2', kwargs={'pk': pk}), context)
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('onboarding_detail2', kwargs={'pk': pk}), context)
    # Get Form Instance to Complete Onboarding
    else:
        if onboarding_checklist[1]:
            onboarding_form = Onboarding_Form()
        else:
            onboarding_form = Onboarding_Form(instance=onboarding_checklist[0])
        context.update({'onboarding_form': onboarding_form})
        onboarding_email = "mailto:attorneyonboarding@huronlawgroup.com"
        context.update({'onboarding_email': onboarding_email})
        return render(request, 'templates/onboarding/onboarding_detail.html', context)


@login_required(login_url=reverse_lazy('login'))
def onboarding_detail2(request, pk=None):
    context = {'title': 'Onboarding'}
    employee = Employee.objects.get(employee_id=pk)
    context.update({'employee': employee})
    onboarding_checklist = Onboarding_Detail_Model.objects.get_or_create(employee_id_id=pk)
    if request.method == "POST":
        form = Onboarding_Form2(request.POST, instance=onboarding_checklist[0])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.employee_id_id = pk
            if obj.send_pp_docs and obj.send_software_docs:
                employee.onboarding_step = "Schedule Training"
            elif obj.send_onboarding_email and (obj.puzzle_form or obj.return_ICA or obj.notify_Huron):
                employee.onboarding_step = "Send Onboarding / Training Docs"
            else:
                employee.onboarding_step = "Administrative Tasks"
            obj.save()
            if obj.onboarding_completed:
                employee.onboarding_complete = True
                employee.save()
                return HttpResponseRedirect(reverse_lazy('attorneys'))
            employee.save()
            return HttpResponseRedirect(reverse_lazy('onboarding'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('onboarding_detail', kwargs={'pk': pk}), context)
    # Get Form Instance to Complete Onboarding
    else:
        if onboarding_checklist[1]:
            onboarding_form = Onboarding_Form()
        else:
            onboarding_form = Onboarding_Form2(instance=onboarding_checklist[0])
        context.update({'onboarding_form': onboarding_form})
        onboarding_email = "mailto:attorneyonboarding@huronlawgroup.com"
        context.update({'onboarding_email': onboarding_email})
        return render(request, 'templates/onboarding/onboarding_detail2.html', context)


@login_required(login_url=reverse_lazy('login'))
def onboarding_text(request, pk=None):
    context = {'title': 'Onboarding'}
    # Get Employee information for onboarding text
    employee = Employee.objects.get(employee_id=pk)
    context.update({'employee': employee})
    if employee.gender == "Male":
        pronoun = "he"
    elif employee.gender == "Female":
        pronoun = "she"
    else:
        pronoun = "they"
    context.update({'pronoun': pronoun})
    employee_more = Employee_More_Model.objects.get_or_create(employee_id=pk)
    if not employee_more[1]:
        employee_add = employee_more[0]
        context.update({'employee_add': employee_add})
    return render(request, 'templates/onboarding/onboarding_text.html', context)


@login_required(login_url=reverse_lazy('login'))
def onboard_complete(request, pk=None):
    context = {'title': 'Onboarding'}
    # Get attorneys hired that have not yet completed onboarding
    employee = Employee.objects.get(employee_id=pk)
    employee.onboarding_complete = True
    employee.save()
    attorney_list = Employee.objects.filter(onboarding_complete=True)
    context.update({'attorney_list': attorney_list})
    return HttpResponseRedirect(reverse_lazy('attorneys'))
    # return render(request, 'templates/attorneys.html')