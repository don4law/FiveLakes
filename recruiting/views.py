# Recruiting Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date
from states.models import State
from FiveLakes.settings import BASE_DIR
from recruiting.models import Applicant, Interview1
from recruiting.forms import Applicant_Form, Applicant_Edit, Interview1_Form


@login_required(login_url=reverse_lazy('login'))
def recruiting_view(request):
    context = {'title': 'Recruiting'}
    if request.method == "POST":
        form = Applicant_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
        return HttpResponseRedirect(reverse_lazy('recruiting'), context)
    else:  # GET
        applicants = Applicant.objects.order_by('last_name')
        context.update({'applicant_list': applicants})
        return render(request, 'templates/recruiting.html', context)


@login_required(login_url=reverse_lazy('login'))
def add_applicant(request):
    context = {'title': 'Recruiting'}
    if request.method == "POST":
        form = Applicant_Form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj_state = obj.state_abbrev
            applicant_manager = State.objects.get(state_abbrev = obj_state).manager
            obj.manager = applicant_manager
            obj.save()
            return HttpResponseRedirect(reverse_lazy('recruiting'), context)
        return HttpResponseRedirect(reverse_lazy('recruiting'), context)
    else:  # GET
        applicantForm = Applicant_Form()
        states = State.objects.order_by('state_abbrev')
        context.update({'states': states})
        context.update({'applicantForm': applicantForm})
        return render(request, 'templates/recruiting/add_applicant.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_applicant(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(id=pk)
    if request.method == "POST":
        form = Applicant_Edit(request.POST, request.FILES, instance=applicant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('recruiting'), context)
        return HttpResponseRedirect(reverse_lazy('recruiting'), context)
    else:  # GET
        ApplicantForm = Applicant_Edit(instance=applicant)
        states = State.objects.order_by('state_abbrev')
        context.update({'states': states})
        context.update({'applicantForm': ApplicantForm})
        return render(request, 'templates/recruiting/edit_applicant.html', context)

@login_required(login_url=reverse_lazy('login'))
def applicant_delete(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(id=pk)
    applicant.delete()
    return HttpResponseRedirect(reverse('recruiting'))


@login_required(login_url=reverse_lazy('login'))
def applicant_detail(request, pk=None):
    context = {'title': 'Recruiting'}
    if request.method == "POST":
        pass
    else:
        applicant = Applicant.objects.get(id=pk)
        context.update({'applicant': applicant})
        Interview1Form = Interview1_Form(instance=applicant)
        context.update({'interview1_form': Interview1Form})
        return render(request, 'templates/recruiting/applicant_detail.html', context)


@login_required(login_url=reverse_lazy('login'))
def applicant_interview1(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(id=pk)
    # Produces a tuple with (object, creation) where creation is a boolean
    # if it was created
    if request.method == "POST":
        form = Interview1_Form(request.POST, instance=applicant)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.applicant_id = pk
            form.save()
            return HttpResponseRedirect(reverse_lazy('recruiting'), context)
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('applicant_interview1', kwargs={'pk': pk}), context)
    else:
        applicant = Applicant.objects.get_or_create(id=pk)
        context.update({'applicant': applicant[0]})
        if applicant[1] == 0: # Object already exists
            Interview1Form = Interview1_Form(instance=applicant[0])
        else: # New object created
            Interview1Form = Interview1_Form()
        context.update({'interview1_form': Interview1Form})
        return render(request, 'templates/recruiting/interview1.html', context)