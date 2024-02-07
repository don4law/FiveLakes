# Recruiting Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date
from itertools import chain
from states.models import State
from FiveLakes.settings import BASE_DIR
from recruiting.models import Applicant, Interview1_Model, Interview2_Model, FinalStep_Model, Search_Model
from recruiting.forms import (Applicant_Form, Applicant_Edit, Interview1_Form, Interview2_Form,
                              FinalStep_Form, Search_Form)
from attorneys.models import Employee


@login_required(login_url=reverse_lazy('login'))
def recruiting_view(request):
    context = {'title': 'Recruiting'}
    search_db = Search_Model.objects.get_or_create(pk=1)
    search_id = search_db[0]
    if request.method == "POST":
        form = Search_Form(request.POST, instance=search_id)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
        return HttpResponseRedirect(reverse_lazy('recruiting'), context)
    else:  # GET
        # Get search form
        searchForm = Search_Form()
        context.update({'searchForm': searchForm})

        search_criteria = Search_Model.objects.get_or_create(pk=1)
        # clear search box
        Search_Model.objects.filter(pk=1).delete()

        if search_criteria[0].search_manager:
            # Get all active applicants for each step in interview process
            applicant_new = Applicant.objects.filter(is_active=True, step='New Resume', manager=search_criteria[0].search_manager).order_by('last_name')
            context.update({'applicant_new_list': applicant_new})

            applicant_interview1 = Applicant.objects.filter(is_active=True, step='Interview1', manager=search_criteria[0].search_manager).order_by('last_name')
            context.update({'interview1_list': applicant_interview1})

            applicant_interview2 = Applicant.objects.filter(is_active=True, step='Interview2', manager=search_criteria[0].search_manager).order_by('last_name')
            context.update({'interview2_list': applicant_interview2})

            applicant_final = Applicant.objects.filter(is_active=True, step='Final', manager=search_criteria[0].search_manager).order_by('last_name')
            context.update({'final_step_list': applicant_final})

            applicant_open = Applicant.objects.filter(is_active=True, step='Open File', manager=search_criteria[0].search_manager).order_by('last_name')
            context.update({'open_file_list': applicant_open})

        # Search by State
        elif search_criteria[0].search_state:
            # Get all active applicants for each step in interview process
            applicant_new = Applicant.objects.filter(is_active=True, step='New Resume', state_abbrev=search_criteria[0].search_state).order_by('last_name')
            context.update({'applicant_new_list': applicant_new})

            applicant_interview1 = Applicant.objects.filter(is_active=True, step='Interview1', state_abbrev=search_criteria[0].search_state).order_by('last_name')
            context.update({'interview1_list': applicant_interview1})

            applicant_interview2 = Applicant.objects.filter(is_active=True, step='Interview2', state_abbrev=search_criteria[0].search_state).order_by('last_name')
            context.update({'interview2_list': applicant_interview2})

            applicant_final = Applicant.objects.filter(is_active=True, step='Final', state_abbrev=search_criteria[0].search_state).order_by('last_name')
            context.update({'final_step_list': applicant_final})

            applicant_open = Applicant.objects.filter(is_active=True, step='Open File', state_abbrev=search_criteria[0].search_state).order_by('last_name')
            context.update({'open_file_list': applicant_open})

        # Search by Step in Recruitment Process
        elif search_criteria[0].search_step:
            # Get all active applicants for each step in interview process
            if search_criteria[0].search_step == "New Resume":
                applicant_new = Applicant.objects.filter(is_active=True, step=search_criteria[0].search_step).order_by('last_name')
                context.update({'applicant_new_list': applicant_new})
            elif search_criteria[0].search_step == "Interview1":
                applicant_interview1 = Applicant.objects.filter(is_active=True, step=search_criteria[0].search_step).order_by('last_name')
                context.update({'interview1_list': applicant_interview1})
            elif search_criteria[0].search_step == "Interview2":
                applicant_interview2 = Applicant.objects.filter(is_active=True, step=search_criteria[0].search_step).order_by('last_name')
                context.update({'interview2_list': applicant_interview2})
            elif search_criteria[0].search_step == "Final":
                applicant_final = Applicant.objects.filter(is_active=True, step=search_criteria[0].search_step).order_by('last_name')
                context.update({'final_step_list': applicant_final})
            elif search_criteria[0].search_step == "Open File":
                applicant_open = Applicant.objects.filter(is_active=True, step=search_criteria[0].search_step).order_by('last_name')
                context.update({'open_file_list': applicant_open})

        # No criteria entered
        else:
            # Get all active applicants for each step in interview process
            applicant_new = Applicant.objects.filter(is_active=True, step='New Resume').order_by('last_name')
            context.update({'applicant_new_list': applicant_new})

            applicant_interview1 = Applicant.objects.filter(is_active=True, step='Interview1').order_by('last_name')
            context.update({'interview1_list': applicant_interview1})

            applicant_interview2 = Applicant.objects.filter(is_active=True, step='Interview2').order_by('last_name')
            context.update({'interview2_list': applicant_interview2})

            applicant_final = Applicant.objects.filter(is_active=True, step='Final').order_by('last_name')
            context.update({'final_step_list': applicant_final})

            applicant_open = Applicant.objects.filter(is_active=True, step='Open File').order_by('last_name')
            context.update({'open_file_list': applicant_open})

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
            applicant = Applicant.objects.get(pk=pk)
            if obj.interview1_completed == False:
                applicant.step = "Interview1"
            else:
                applicant.step = "Interview2"
            applicant.save()
            obj.save()
            return HttpResponseRedirect(reverse_lazy('applicant_detail', kwargs={'pk': pk}), context)
        else:
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
            applicant = Applicant.objects.get(pk=pk)
            if obj.interview2_completed == False:
                applicant.step = "Interview2"
            else:
                applicant.step = "Final"
            applicant.save()
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
            applicant = Applicant.objects.get(pk=pk)
            if obj.completed == False:
                applicant.step = "Final"
            else:
                applicant.step = "Open File"
            applicant.save()
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
    # Get objects to complete new hire file
    applicant_data = Applicant.objects.get(pk=pk)
    applicant_start_date = FinalStep_Model.objects.get(applicant_id=pk).start_date
    new_hire = Employee.objects.get_or_create(employee_id=pk)

    # Fill new hire object with Applicant Data
    new_hire[0].is_active = True
    new_hire[0].state_abbrev = applicant_data.state_abbrev
    new_hire[0].position = applicant_data.position
    new_hire[0].salary = applicant_data.salary
    new_hire[0].manager = applicant_data.manager
    new_hire[0].gender = applicant_data.gender
    new_hire[0].first_name = applicant_data.first_name
    new_hire[0].middle_name = applicant_data.middle_name
    new_hire[0].last_name = applicant_data.last_name
    new_hire[0].phone = applicant_data.phone
    new_hire[0].email = applicant_data.email
    new_hire[0].five_lakes_firm = applicant_data.five_lakes_firm
    new_hire[0].huron_firm = applicant_data.huron_firm
    new_hire[0].resume = applicant_data.resume
    new_hire[0].hire_date = date.today()
    new_hire[0].start_date = applicant_start_date
    new_hire[0].onboarding_complete = False
    new_hire[0].save()

    # Change status of Applicant to Inactive if Retain in file
    # Otherwise, delete the Applicant file
    interview1_retain = Interview1_Model.objects.get(applicant_id=pk).retain_in_file
    interview2_retain = Interview1_Model.objects.get(applicant_id=pk).retain_in_file
    if interview1_retain or interview2_retain:
        obj = Applicant.objects.get(pk=pk)
        obj.is_active = False
        obj.save()
    else:
        Applicant.objects.get(pk=pk).delete()
        Interview1_Model.objects.get(applicant_id=pk).delete()
        Interview2_Model.objects.get(applicant_id=pk).delete()
        FinalStep_Model.objects.get(applicant_id=pk).delete()
    return render(request, 'templates/recruiting.html')
