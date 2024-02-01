# Recruiting Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date
from states.models import State
from FiveLakes.settings import BASE_DIR
from recruiting.models import Applicant, Interview1_Model, Interview2_Model, FinalStep_Model
from recruiting.forms import Applicant_Form, Applicant_Edit, Interview1_Form, Interview2_Form, FinalStep_Form


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
        Interview1_Detail = Interview1_Model.objects.get_or_create(applicant_id=pk)
        context.update({'interview1': Interview1_Detail[0]})
        Interview2_Detail = Interview2_Model.objects.get_or_create(applicant_id=pk)
        context.update({'interview2': Interview2_Detail[0]})
        Final_Step_Detail = FinalStep_Model.objects.get_or_create(applicant_id=pk)
        context.update({'final_step': Final_Step_Detail[0]})
        return render(request, 'templates/recruiting/applicant_detail.html', context)


@login_required(login_url=reverse_lazy('login'))
def applicant_interview1(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(pk=pk)
    context.update({'applicant': applicant})
    applicant_interview = Interview1_Model.objects.get_or_create(applicant_id=pk)
    # Produces a tuple with (object, creation) where creation is a boolean
    # if it was created
    if request.method == "POST":
        form = Interview1_Form(request.POST, instance=applicant_interview[0])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.applicant_id = pk
            obj.save()
            return HttpResponseRedirect(reverse_lazy('applicant_detail', kwargs={'pk': pk}), context)
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('applicant_interview1', kwargs={'pk': pk}), context)
    else: #GET
        form = Interview1_Form(instance=applicant_interview[0])
        context.update({'interview1_form': form})
        return render(request, 'templates/recruiting/interview1.html', context)

# Function to generate decline email text on blank page
@login_required(login_url=reverse_lazy('login'))
def int1_decline_text(request, pk=None):
    applicant = Applicant.objects.get(pk=pk)
    context = {'applicant': applicant}
    return render(request, 'templates/recruiting/interview1_decline.html', context)

@login_required(login_url=reverse_lazy('login'))
def applicant_interview2(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(pk=pk)
    context.update({'applicant': applicant})
    applicant_interview = Interview2_Model.objects.get_or_create(applicant_id=pk)
    # Produces a tuple with (object, creation) where creation is a boolean
    # if it was created
    if request.method == "POST":
        form = Interview2_Form(request.POST, instance=applicant_interview[0])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.applicant_id = pk
            obj.save()
            return HttpResponseRedirect(reverse_lazy('applicant_detail', kwargs={'pk': pk}), context)
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('applicant_interview1', kwargs={'pk': pk}), context)
    else: #GET
        form = Interview2_Form(instance=applicant_interview[0])
        context.update({'interview2_form': form})
        return render(request, 'templates/recruiting/interview2.html', context)

@login_required(login_url=reverse_lazy('login'))
def int2_decline_text(request, pk=None):
    applicant = Applicant.objects.get(pk=pk)
    context = {'applicant': applicant}
    return render(request, 'templates/recruiting/interview2_decline.html', context)


# @login_required(login_url=reverse_lazy('login'))
# def final_wrapup(request, pk=None):
#     applicant = Applicant.objects.get(pk=pk)
#     context = {'applicant': applicant}
#     return render(request, 'templates/recruiting/final_wrapup.html', context)


@login_required(login_url=reverse_lazy('login'))
def applicant_final_step(request, pk=None):
    context = {'title': 'Recruiting'}
    applicant = Applicant.objects.get(pk=pk)
    context.update({'applicant': applicant})
    applicant_final_step = FinalStep_Model.objects.get_or_create(applicant_id=pk)
    # Produces a tuple with (object, creation) where creation is a boolean
    # if it was created
    if request.method == "POST":
        form = FinalStep_Form(request.POST, instance=applicant_final_step[0])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.applicant_id = pk
            obj.save()
            return HttpResponseRedirect(reverse_lazy('applicant_detail', kwargs={'pk': pk}), context)
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse_lazy('applicant_final_step', kwargs={'pk': pk}), context)
    else: #GET
        form = FinalStep_Form(instance=applicant_final_step[0])
        context.update({'final_step_form': form})
        return render(request, 'templates/recruiting/final_wrapup.html', context)

@login_required(login_url=reverse_lazy('login'))
def offer_letter_text(request, pk=None):
    applicant = Applicant.objects.get(pk=pk)
    context = {'applicant': applicant}
    offer_data = FinalStep_Model.objects.get(applicant_id=pk)
    context.update({'offer': offer_data})
    return render(request, 'templates/recruiting/offer_letter_text.html', context)


# Function to make applicant inactive and move info to Employee
@login_required(login_url=reverse_lazy('login'))
def create_employee_file(request, pk=None):
    pass
    return render(request, 'templates/recruiting/offer_letter_text.html', context)
