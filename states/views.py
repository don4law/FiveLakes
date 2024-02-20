# State Data Views
from django.db.migrations import state
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date

from attorneys.models import Employee
from states.models import State
from states.forms import State_Form


@login_required(login_url=reverse_lazy('login'))
def states_view(request):
    context = {'title': 'State Data'}
    states = State.objects.order_by('state_abbrev')
    # ADD TO CONTEXT: Actual counts of employees by State abd Type
    for state in states:
        full_time_actual = 0
        part_time_actual = 0
        of_counsel_actual = 0
        floater_actual = 0
        FTE_actual = 0
        for employee in Employee.objects.filter(state_abbrev=state.state_abbrev, is_active=True):
            if employee.position == "Full-Time":
                full_time_actual += 1
                FTE_actual += 1
            if employee.position == "Part-Time":
                part_time_actual += 1
                FTE_actual += .5
            if employee.position == "Of Counsel":
                of_counsel_actual += 1
                FTE_actual += .5
            if employee.position == "Floater":
                floater_actual += 1
                FTE_actual += 0
        FTE_actual = full_time_actual + part_time_actual + of_counsel_actual + floater_actual
        setattr(state, "full_time_actual", full_time_actual)
        print(state.state_abbrev, state.full_time_actual)
        setattr(state, "part_time_actual", part_time_actual)
        setattr(state, "of_counsel_actual", of_counsel_actual)
        setattr(state, "floater_actual", floater_actual)
        setattr(state, "FTE_actual", FTE_actual)
    context.update({'states': states})
    if request.method == "POST":
        form = State_Form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('states'), context)
    else:  # GET
        stateForm = State_Form()
        context.update({'stateForm': stateForm})
        return render(request, 'templates/states.html', context)


@login_required(login_url=reverse_lazy('login'))
def add_states(request, search_state=None, search_manager=None, search_priority=None):
    context = {'title': 'State Data'}
    states = State.objects.order_by('state_abbrev')
    context.update({'states': states})
    if request.method == "POST":
        form = State_Form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('states'), context)
    else:  # GET
        stateForm = State_Form()
        states = State.objects.order_by('state_abbrev')
        context.update({'states': states})
        context.update({'stateForm': stateForm})
        return render(request, 'templates/states/add_states.html', context)


@login_required(login_url=reverse_lazy('login'))
def edit_state(request, pk=None):
    title = 'State Data'
    context = {'title': 'State Data'}
    states = State.objects.order_by('state_abbrev')
    context.update({'states': states})
    state = State.objects.get(state_abbrev=pk)
    if request.method == "POST":
        stateForm = State_Form(request.POST, instance=state)
        if stateForm.is_valid():
            stateForm.save()
        return redirect('states')
    else:  # GET
        stateForm = State_Form(instance=state)
        context = {'title': title, 'state': state, 'stateForm': stateForm}
        return render(request, 'templates/states/edit_state.html', context)

