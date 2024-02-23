# Attorneys Views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import datetime, date
from django.forms import inlineformset_factory
from managers.models import CustomUser
from attorneys.models import Employee, Search_Attorneys_Model, QA_Model, \
    HR_Requests_Model, Call_Monitoring_Model, Attorney_Notes_Model, Employee_More_Model, \
    To_Do_Model, Metrics_Model
from attorneys.forms import Search_Attorneys_Form, QA_Form, HR_Form, Call_Form, Attorney_Notes_Form, \
    Edit_EmployeeForm1, Employee_More_Form, To_Do_Form, Metric_Form

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
    # CODE TO GET TICKLER FOR MAIN ATTORNEY PAGE
    # First, get manager's name to join with name for employee/attorney
    manager_id = request.user.id
    context.update({'manager_id': manager_id})
    manager_user = CustomUser.objects.get(id = manager_id)
    manager_name = manager_user.first_name + " " + manager_user.last_name
    # Second, get list of all employees/attorneys managed by logged in Manager
    employee_list = []
    for employee in Employee.objects.all():
        if employee.manager == manager_name:
            employee_list.append(employee.employee_id)
    # Third, get all user notes for employees
    user_notes_list = Attorney_Notes_Model.objects.filter(employee_id_id__in=employee_list,
                    follow_up_required=True, follow_up_completed=False).order_by('date')
    # Now need name of each employee for each tickler note in the NOTE for template
    for note in user_notes_list:
        for employee in Employee.objects.all():
            if note.employee_id_id == employee.employee_id:
                setattr(note, "employee_name", employee.first_name + " " + employee.last_name)
    tickler_list = user_notes_list
    context.update({'tickler_list': tickler_list})

    # Get Each Managers task list
    to_do_list = To_Do_Model.objects.filter(employee_id_id = manager_id)
    # Now need name of each employee for each tickler note in the NOTE for template
    for to_do in to_do_list:
        for employee in Employee.objects.all():
            if to_do.employee_id_id == employee.employee_id:
                setattr(employee, "employee_name", employee.first_name + " " + employee.last_name)
    to_do = to_do_list
    context.update({'to_do_list': to_do})
    return render(request, 'templates/attorneys.html', context)


# View to edit all attorney profile data and return to onboarding
@login_required(login_url=reverse_lazy('login'))
def add_attorney_more_onboarding(request, pk=None, prev=None):
    context = {'title': 'Attorneys'}
    employee_main = Employee.objects.get(pk=pk)
    context.update({'employee': employee_main})
    attorney_data = Employee_More_Model.objects.get_or_create(employee_id=pk)
    context.update({'attorney': attorney_data[0]})
    if request.method == "POST":
        form = Employee_More_Form(request.POST, request.FILES)
        form.instance.employee_id = pk
        if form.is_valid():
            form.save()
            print('saved')
        else:
            context.update({'form': form})
        return HttpResponseRedirect(reverse_lazy('onboarding_detail', kwargs={'pk': pk}), context)
    else:  # GET
        if attorney_data[1]:
            MoreForm = Employee_More_Form()
        else:
            MoreForm = Employee_More_Form(instance=attorney_data[0])
        context.update({'moreForm': MoreForm})
        return render(request, 'templates/attorneys/more_attorney_data.html', context)


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
        metrics_list = Metrics_Model.objects.filter(employee_id=pk).order_by('-date')
        context.update({'metrics': metrics_list})
        attorney_QA = QA_Model.objects.filter(employee_id=pk).order_by('-qa_date')
        context.update({'attorney_QA': attorney_QA})
        hr_requests = HR_Requests_Model.objects.filter(employee_id=pk).order_by('-date')
        context.update({'hr_requests': hr_requests})
        call_requests = Call_Monitoring_Model.objects.filter(employee_id=pk).order_by('-date')
        context.update({'call_requests': call_requests})
        attorney_notes = Attorney_Notes_Model.objects.filter(employee_id=pk).order_by('-date')
        context.update({'attorney_notes': attorney_notes})
        # GET BLANK FORMS TO ADD ATTORNEY DATA
        # GET form to add new instance for Metrics
        MetricsForm = Metric_Form()
        context.update({'MetricsForm': MetricsForm})
        # GET form to add new instance in QA
        QAForm = QA_Form()
        context.update({'QAForm': QAForm})
        # GET form to add new instance for Flex/PTO Time
        HRForm = HR_Form()
        context.update({'HRForm': HRForm})
        # GET form to add new instance for Call Monitoring
        CallForm = Call_Form()
        context.update({'CallForm': CallForm})
        # GET form to add new instance for Notes
        NotesForm = Attorney_Notes_Form()
        context.update({'NotesForm': NotesForm})
        return render(request, 'templates/attorneys/attorney_data.html', context)


# edit_attorney_all (To edit All Attorney Info: Employee Model and Employee_More Model
@login_required(login_url=reverse_lazy('login'))
def edit_attorney_profile(request, pk=None, prev_page=None):
    context = {'title': 'Attorneys'}
    attorney_data1 = Employee.objects.get(employee_id=pk)
    attorney_data2 = Employee_More_Model.objects.get_or_create(employee_id=pk)
    context.update({'attorney': attorney_data1})
    context.update({'attorney2': attorney_data2[0]})
    if request.method == "POST":
        form1 = Edit_EmployeeForm1(request.POST, request.FILES, instance=attorney_data1)
        form2 = Employee_More_Form(request.POST, request.FILES, instance=attorney_data2[0])
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            print(obj1.prev_page)
            if obj1.resume is None:
                obj1.instance.resume = attorney_data1.resume
            obj1.save()
            form2.save()
            attorney_data1 = Employee.objects.get(employee_id=pk)
            if attorney_data1.prev_page:
                return redirect(attorney_data1.prev_page)
        return HttpResponseRedirect(reverse_lazy('attorneys'))
    else: # GET
        attorney_data1 = Employee.objects.get(employee_id=pk)
        attorney_data1.prev_page = request.META.get('HTTP_REFERER')
        attorney_data1.save()
        context.update({'attorney_data1': attorney_data1})
        context.update({'attorney_data2': attorney_data2[0]})
        # GET form to edit Employee Data and Employee_More Data
        AttorneyForm1 = Edit_EmployeeForm1(instance=attorney_data1)
        AttorneyForm2 = Employee_More_Form(instance=attorney_data2[0])
        context.update({'attorneyForm1': AttorneyForm1})
        context.update({'attorneyForm2': AttorneyForm2})
        return render(request, 'templates/attorneys/edit_attorney_profile.html', context)


@login_required(login_url=reverse_lazy('login'))
def add_note(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Attorney_Notes_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
            print('saved')
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
    else:
        NoteForm = Attorney_Notes_Form(instance=attorney_data)
        context.update({'noteForm': NoteForm})
        return render(request, 'templates/attorneys/add_attorney_note.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_note(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Attorney_Notes_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
            print('saved')
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)
    else:
        note_instance = Attorney_Notes_Model.objects.get(id=pk)
        NoteForm = Attorney_Notes_Form(instance=note_instance)
        context.update({'noteForm': NoteForm})
        # return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
        return render(request, 'templates/attorneys/edit_attorney_note.html', context)

@login_required(login_url=reverse_lazy('login'))
def add_call(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Call_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
    else:
        CallForm = Call_Form(instance=attorney_data)
        context.update({'callForm': CallForm})
        return render(request, 'templates/attorneys/add_call.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_call(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Call_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)
    else:
        call_instance = Call_Monitoring_Model.objects.get(id=pk)
        CallForm = Call_Form(instance=call_instance)
        context.update({'callForm': CallForm})
        # return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
        return render(request, 'templates/attorneys/edit_call.html', context)

@login_required(login_url=reverse_lazy('login'))
def add_coaching(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = QA_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
    else:
        QAForm = QA_Form(instance=attorney_data)
        context.update({'qaForm': QAForm})
        return render(request, 'templates/attorneys/add_qa.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_coaching(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = QA_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)
    else:
        qa_instance = QA_Model.objects.get(id=pk)
        QAForm = QA_Form(instance=qa_instance)
        context.update({'qaForm': QAForm})
        return render(request, 'templates/attorneys/edit_qa.html', context)

@login_required(login_url=reverse_lazy('login'))
def add_todo(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = To_Do_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorneys'))
    else:
        ToDoForm = To_Do_Form(instance=attorney_data)
        context.update({'todoForm': ToDoForm})
        return render(request, 'templates/attorneys/add_todo.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_task(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = To_Do_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorneys'))
    else:
        task_instance = To_Do_Model.objects.get(id=pk)
        TaskForm = To_Do_Form(instance=task_instance)
        context.update({'todoForm': TaskForm})
        return render(request, 'templates/attorneys/edit_todo.html', context)


@login_required(login_url=reverse_lazy('login'))
def delete_task(request, pk=None):
    context = {'title': 'Attorneys'}
    task = To_Do_Model.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect(reverse('attorneys'))

@login_required(login_url=reverse_lazy('login'))
def add_metric(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Metric_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
    else:
        MetricForm = Metric_Form(instance=attorney_data)
        context.update({'metricForm': MetricForm})
        return render(request, 'templates/attorneys/add_metric.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_metric(request, pk=None, employee=None):
    context = {'title': 'Edit Metric'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = Metric_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)
    else:
        metric_instance = Metrics_Model.objects.get(id=pk, employee_id=employee)
        metricForm = Metric_Form(instance=metric_instance)
        context.update({'metricForm': metricForm})
    return render(request, 'templates/attorneys/edit_metric.html', context)

@login_required(login_url=reverse_lazy('login'))
def delete_metric(request, pk=None):
    context = {'title': 'Attorneys'}
    metric = Metrics_Model.objects.get(id=pk)
    metric.delete()
    return HttpResponseRedirect(reverse('attorneys'))

@login_required(login_url=reverse_lazy('login'))
def delete_note(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    note = Attorney_Notes_Model.objects.get(id=pk)
    note.delete()
    return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)


@login_required(login_url=reverse_lazy('login'))
def delete_QA(request, pk=None, employee=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    qa = QA_Model.objects.get(id=pk)
    qa.delete()
    return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)

@login_required(login_url=reverse_lazy('login'))
def add_hr(request, pk=None):
    context = {'title': 'Attorneys'}
    attorney_data = Employee.objects.get(employee_id=pk)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = HR_Form(request.POST, request.FILES)
        form.instance.employee_id_id = pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': pk}), context)
    else:
        HRForm = HR_Form(instance=attorney_data)
        context.update({'hrForm': HRForm})
        return render(request, 'templates/attorneys/add_hr.html', context)

@login_required(login_url=reverse_lazy('login'))
def edit_hr(request, pk=None, employee=None):
    context = {'title': 'Edit Metric'}
    attorney_data = Employee.objects.get(employee_id=employee)
    context.update({'attorney': attorney_data})
    if request.method == "POST":
        form = HR_Form(request.POST, request.FILES)
        form.instance.id = pk
        form.instance.employee_id_id = employee
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('attorney_data', kwargs={'pk': employee}), context)
    else:
        hr_instance = HR_Requests_Model.objects.get(id=pk, employee_id=employee)
        hrForm = HR_Form(instance=hr_instance)
        context.update({'hrForm': hrForm})
    return render(request, 'templates/attorneys/edit_hr.html', context)