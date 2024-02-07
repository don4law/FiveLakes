# attorneys.forms

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, Div, \
    Field, HTML
from states.models import get_managers
from attorneys.models import Employee, Search_Attorneys_Model, QA_Model, \
    HR_Requests_Model, Call_Monitoring_Model

# Alphabetized list of managers for choices
managers=get_managers()


class Search_Attorneys_Form(ModelForm):
    class Meta:
        model = Search_Attorneys_Model
        fields = ['search_manager', 'search_state', 'search_priority']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('search_manager',
                       css_class='form-group col-md-4 mb-0'),
                Column('search_state',
                       css_class='form-group col-md-4 mb-0'),
                Column('search_priority',
                       css_class='form-group col-md-4 mb-0'),
            ),
        )

class QA_Form(ModelForm):
    class Meta:
        model = QA_Model
        fields = ('qa_date', 'qa_time', 'method',
                  'related_to', 'delivered_by',
                  'qa_note', 'document')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('qa_date',
                       css_class='form-group col-md-4 mb-0'),
                Column('qa_time',
                       css_class='form-group col-md-4 mb-0'),
                Column('method',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('related_to',
                       css_class='form-group col-md-4 mb-0'),
                Column('delivered_by',
                       css_class='form-group col-md-4 mb-0'),
                Column('document',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('qa_note',
                       css_class='form-group col-md-12 mb-0'),
                ),
        )

class HR_Form(ModelForm):
    class Meta:
        model = HR_Requests_Model
        fields = ('date', 'time', 'request_type',
                  'request_note', 'approved',
                  'denied', 'document', 'reasoning',
                  'decision_manager')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('date',
                       css_class='form-group col-md-3 mb-0'),
                Column('time',
                       css_class='form-group col-md-3 mb-0'),
                Column('request_type',
                       css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('request_note',
                       css_class='form-group col-md-6 mb-0'),
                Column('approved',
                       css_class='form-group col-md-2 mb-0'),
                Column('denied',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('reasoning',
                       css_class='form-group col-md-6 mb-0'),
                Column('document',
                       css_class='form-group col-md-3 mb-0'),
                Column('decision_manager',
                       css_class='form-group col-md-3 mb-0'),
            ),
        )

class Call_Form(ModelForm):
    class Meta:
        model = Call_Monitoring_Model
        fields = ('date', 'call_date', 'call_time', 'duration',
                  'disposition', 'notes', 'document', 'reviewer')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('date',
                       css_class='form-group col-md-3 mb-0'),
                Column('call_date',
                       css_class='form-group col-md-3 mb-0'),
                Column('call_time',
                       css_class='form-group col-md-3 mb-0'),
                Column('duration',
                       css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('notes',
                       css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('disposition',
                       css_class='form-group col-md-4 mb-0'),
                Column('document',
                       css_class='form-group col-md-4 mb-0'),
                Column('reviewer',
                       css_class='form-group col-md-4 mb-0'),
            ),
        )