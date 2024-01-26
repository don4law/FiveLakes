from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, Div, \
    Field, HTML
from states.models import State


class State_Form(ModelForm):

    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('state_abbrev',
                       css_class='form-group col-md-2 mb-0'),
                Column('state_full',
                       css_class='form-group col-md-4 mb-0'),
                Column('state_status',
                       css_class='form-group col-md-2 mb-0'),
                Column('manager',
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column(HTML('Check all position types that apply:'),
                       css_class='form-group col-md-3 mb-0'),
                Column('full_time',
                       css_class='form-group col-md-2 mb-0'),
                Column('part_time',
                       css_class='form-group col-md-2 mb-0'),
                Column('of_counsel',
                       css_class='form-group col-md-2 mb-0'),
                Column('floater',
                       css_class='form-group col-md-2 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('recruiting_status',
                       css_class='form-group col-md-2 mb-0'),
                Column('state_priority',
                       css_class='form-group col-md-2 mb-0'),
                ),
            )