# onboarding.forms

from django.forms import ModelForm
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
        fields = ['pause_job', 'send_onboarding_email', 'add_to_spreadsheet',
                  'save_license', 'bar_license_document', 'onboarding_completed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('pause_job',
                   HTML('<a href = "mailto:attorneyonboarding@huronlawgroup.com"></a>'),
                   css_class='form-group col-md-12 mb-0'),
                ),
            Row(
                Column(HTML('<a href = "mailto:attorneyonboarding@huronlawgroup.com"></a>'),
                        css_class='form-group col-md-12 mb-0'),
                ),
        )
            # Row(
            #     Column('send_onboarding_email',
            #            css_class='form-group col-md-2 mb-0'),
            # ),
            #     Column('add_to_spreadsheet',
            #            css_class='form-group col-md-2 mb-0'),
            # ),
            # Row(
            #     Column('save_license',
            #            css_class='form-group col-md-2 mb-0'),
            #     Column('bar_license_document',
            #            css_class='form-group col-md-2 mb-0'),
            # ),
            # Row(
            #     Column('onboarding_completed',
            #            css_class='form-group col-md-2 mb-0'),
            #     ),
        # )

