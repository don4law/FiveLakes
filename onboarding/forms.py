# onboarding.forms

from django.forms import ModelForm, forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit, Row, Column, Div, \
    Field, HTML
from states.models import get_managers
from onboarding.models import Onboarding_Detail_Model

# Alphabetized list of managers for choices
managers=get_managers()

class Onboarding_Form(ModelForm):
    class Meta:
        model = Onboarding_Detail_Model
        fields = ['add_attorney_more', 'pause_job', 'send_onboarding_email', 'add_to_spreadsheet', 'send_spreadsheet',
                  'save_license', 'onboarding_completed',
                  'save_offer_letter', 'puzzle_form', 'include_note',
                  'attach_copy_letter', 'employee_referral_form', 'return_ICA', 'notify_Huron',]

class Onboarding_Form2(ModelForm):
    class Meta:
        model = Onboarding_Detail_Model
        fields = ['send_pp_docs', 'send_software_docs', 'intro_training',
                  'intro_training_date', 'salesforce_training', 'salesforce_training_date',
                  'script_training', 'script_training_date', 'attorney_pp_training', 'attorney_pp_date',
                  'touchbase_meeting', 'touchbase_date', 'onboarding_completed',]


