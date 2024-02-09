# Attorneys Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import datetime, date
from django.forms import inlineformset_factory
from managers.models import CustomUser
from attorneys.models import Employee, Search_Attorneys_Model, QA_Model, \
    HR_Requests_Model, Call_Monitoring_Model, Attorney_Notes_Model
from attorneys.forms import Search_Attorneys_Form, QA_Form, HR_Form, \
    Call_Form, Attorney_Notes_Form

@login_required(login_url=reverse_lazy('login'))
def attorney_view(request):
  context = {'title': 'Attorneys'}
  # Get search form
  search_db = Search_Attorneys_Model.objects.get_or_create(pk=1)
  search_id = search_db[0]
  if request.method == "POST":
    form = Search_Attorneys_Form(request.POST, instance=search_id)
    if form.is_valid():
      form.save()
    else:
      context.update({'form': form})
    return HttpResponseRedirect(reverse_lazy('attorneys'), context)
  else:  # GET
    # Get search form
    searchForm = Search_Attorneys_Form()
    context.update({'searchForm': searchForm})
    search_criteria = Search_Attorneys_Model.objects.get_or_create(pk=1)
    # clear search box
    Search_Attorneys_Model.objects.filter(pk=1).delete()
    attorneys = Employee.objects.filter(onboarding_complete=True, is_active=True).order_by('last_name', 'first_name')
    if search_criteria[0].search_manager:
        # Get all active employees for manager selected or ALL
        attorneys = Employee.objects.filter(onboarding_complete=True,is_active=True,
                manager=search_criteria[0].search_manager).order_by('last_name', 'first_name')
        context.update({'search_criteria': 'manager'})
        context.update({'search_term': search_criteria[0].search_manager})
    if search_criteria[0].search_state:
        attorneys=attorneys.filter(state_abbrev=search_criteria[0].search_state)
        context.update({'search_criteria': 'state'})
        context.update({'search_term': search_criteria[0].search_state})
    if search_criteria[0].search_priority:
        attorneys=attorneys.filter(priority=search_criteria[0].search_priority)
        context.update({'search_criteria': 'priority'})
        context.update({'search_term': search_criteria[0].search_priority})
    context.update({'attorney_list': attorneys})

    # First, current logged in manager id associated with attorney/employee to
    # Filter the NOTES list, then filter the list.
    manager_user = CustomUser.objects.get(id = request.user.id)
    manager_name = manager_user.first_name + " " + manager_user.last_name
    for employee in Employee.objects.all():
        if employee.manager == manager_name:
            manager_id = employee.employee_id
    user_notes_list = Attorney_Notes_Model.objects.filter(employee_id_id = manager_id, follow_up_required=True).order_by('date')

    # Now need name of each employee for each tickler note in the NOTE for template
    for notes in user_notes_list:
        for employee in Employee.objects.all():
            if notes.employee_id_id == employee.employee_id:
                setattr(notes, "employee_name", employee.first_name + " " + employee.last_name)

    tickler_list = user_notes_list
    context.update({'tickler_list': tickler_list})
    return render(request, 'templates/attorneys.html', context)


@login_required(login_url=reverse_lazy('login'))
def attorney_data(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(pk=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = QA_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
            print('Form 1 saved')
        form2 = HR_Form(request.POST, request.FILES)
        form2.instance.employee_id_id = pk
        if form2.is_valid():
            form2.save()
            print('Form 2 saved')
        form3 = Call_Form(request.POST, request.FILES)
        form3.instance.employee_id_id = pk
        if form3.is_valid():
            form3.save()
        form4 = Attorney_Notes_Form(request.POST, request.FILES)
        form4.instance.employee_id_id = pk
        if form4.is_valid():
            form4.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
        # else:
        #     print(form.errors)
        #     return HttpResponseRedirect(reverse_lazy('attorneys'), context)

    else:
        # Filter Data for context
        attorney_QA = QA_Model.objects.filter(employee_id=pk).order_by('qa_date')
        context.update({'attorney_QA': attorney_QA})
        hr_requests = HR_Requests_Model.objects.filter(employee_id=pk).order_by('date')
        context.update({'hr_requests': hr_requests})
        call_requests = Call_Monitoring_Model.objects.filter(employee_id=pk).order_by('date')
        context.update({'call_requests': call_requests})
        attorney_notes = Attorney_Notes_Model.objects.filter(employee_id=pk).order_by('date')
        context.update({'attorney_notes': attorney_notes})
        # GET form to add new instance in QA
        QAForm = QA_Form()
        context.update({'QAForm': QAForm})
        # GET form to add new instance for Flex/PTO Time
        HRForm = HR_Form()
        context.update({'HRForm': HRForm})
        # GET form to add new instance for Flex/PTO Time
        CallForm = Call_Form()
        context.update({'CallForm': CallForm})
        # GET form to add new instance for Flex/PTO Time
        NotesForm = Attorney_Notes_Form()
        context.update({'NotesForm': NotesForm})
        return render(request, 'templates/attorneys/attorney_data.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_attorney_QA(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = QA_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
            print('saved')
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
        # else:
        #     print(form.errors)
        #     return HttpResponseRedirect(reverse_lazy('attorneys'), context)

    else:
        # Filter Attorney's Coaching and QA Data for context
        attorney_QA = QA_Model.objects.filter(employee_id=pk).order_by('qa_date')
        context.update({'attorney_QA': attorney_QA})
        # GET form to add new instance in QA
        QAForm = QA_Form(instance=attorney_data)
        context.update({'QAForm': QAForm})
        return render(request, 'templates/attorneys/attorney_data.html', context)

