# recruiting.forms

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, Div, \
    Field, HTML
from states.models import get_managers
from recruiting.models import Applicant, Interview1_Model, Interview2_Model, FinalStep_Model

# Alphabetized list of managers for choices
managers=get_managers()

class Applicant_Form(ModelForm):

    class Meta:
        model = Applicant
        fields = ['state_abbrev', 'position', 'five_lakes_firm',
                  'huron_firm', 'gender', 'first_name', 'middle_name',
                  'last_name', 'phone', 'email', 'source', 'employee_referral_name',
                  'salary', 'resume', 'initial_notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('state_abbrev',
                       css_class='form-group col-md-2 mb-0'),
                Column('position',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('five_lakes_firm',
                       css_class='form-group col-md-2 mb-0'),
                Column('huron_firm',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('gender',
                       css_class='form-group col-md-2 mb-0'),
                Column('first_name',
                       css_class='form-group col-md-4 mb-0'),
                Column('middle_name',
                       css_class='form-group col-md-2 mb-0'),
                Column('last_name',
                       css_class='form-group col-md-4 mb-0'),
                ),
            Row(
                Column('phone',
                       css_class='form-group col-md-4 mb-0'),
                Column('email',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('source',
                       css_class='form-group col-md-3 mb-0'),
                Column('employee_referral_name',
                       css_class='form-group col-md-3 mb-0'),
                Column('salary',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('resume',
                       css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('initial_notes',
                       css_class='form-group col-md-12 mb-0'),
            ),
        )

class Applicant_Edit(ModelForm):

    class Meta:
        model = Applicant
        fields = ['state_abbrev', 'position', 'manager', 'five_lakes_firm',
                  'huron_firm', 'gender', 'first_name', 'middle_name',
                  'last_name', 'phone', 'email', 'source', 'employee_referral_name',
                  'salary', 'resume', 'initial_notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('state_abbrev',
                       css_class='form-group col-md-2 mb-0'),
                Column('position',
                       css_class='form-group col-md-2 mb-0'),
                Column('manager',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('five_lakes_firm',
                       css_class='form-group col-md-2 mb-0'),
                Column('huron_firm',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('gender',
                       css_class='form-group col-md-2 mb-0'),
                Column('first_name',
                       css_class='form-group col-md-4 mb-0'),
                Column('middle_name',
                       css_class='form-group col-md-2 mb-0'),
                Column('last_name',
                       css_class='form-group col-md-4 mb-0'),
                ),
            Row(
                Column('phone',
                       css_class='form-group col-md-4 mb-0'),
                Column('email',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('source',
                       css_class='form-group col-md-3 mb-0'),
                Column('employee_referral_name',
                       css_class='form-group col-md-3 mb-0'),
                Column('salary',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('resume',
                       css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('initial_notes',
                       css_class='form-group col-md-12 mb-0'),
            ),
        )

class Interview1_Form(ModelForm):

    class Meta:
        model = Interview1_Model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                # Column('applicant_id',
                #        css_class='form-group col-md-4 mb-0'),
                Column('interview1_scheduled',
                       css_class='form-group col-md-4 mb-0'),
                Column('interview1_date',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('interviewer1_manager',
                       css_class='form-group col-md-8 mb-0'),
                Column('interview1_notes',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('approved_to_continue',
                       css_class='form-group col-md-2 mb-0'),
                Column('decline_email_sent',
                       css_class='form-group col-md-2 mb-0'),
                Column('retain_in_file',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('interview1_completed',
                       css_class='form-group col-md-4 mb-0'),
            ),
        )

class Interview2_Form(ModelForm):
    class Meta:
        model = Interview2_Model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                # Column('applicant_id',
                #        css_class='form-group col-md-4 mb-0'),
                Column('interview2_scheduled',
                       css_class='form-group col-md-4 mb-0'),
                Column('interview2_date',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('interviewer2_manager1',
                       css_class='form-group col-md-8 mb-0'),
                Column('interview2_notes1',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('interviewer2_manager2',
                       css_class='form-group col-md-8 mb-0'),
                Column('interview2_notes2',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('approved_to_continue',
                       css_class='form-group col-md-2 mb-0'),
                Column('decline_email_sent',
                       css_class='form-group col-md-2 mb-0'),
                Column('retain_in_file',
                       css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('interview2_completed',
                       css_class='form-group col-md-4 mb-0'),
            ),
        )

class FinalStep_Form(ModelForm):
    class Meta:
        model = FinalStep_Model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('applicant_withdrawn',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('start_date',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('offer_letter_email_date',
                       css_class='form-group col-md-3 mb-0'),
                Column('offer_letter_sent_charles',
                       css_class='form-group col-md-3 mb-0'),
                Column('offer_letter_sent_applicant',
                       css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('offer_accepted',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('completed',
                       css_class='form-group col-md-4 mb-0'),
            ),
        )