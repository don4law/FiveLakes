# managers/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms import bootstrap, helper, layout
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, Div, \
    Field, HTML


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('email',
                       css_class='form-group col-md-4 mb-0'),
                Column('first_name',
                       css_class='form-group col-md-4 mb-0'),
                Column('last_name',
                       css_class='form-group col-md-4 mb-0'),
            ))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_tag = False
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                Row(
                    Column('email',
                           css_class='form-group col-md-4 mb-0'),
                    Column('first_name',
                           css_class='form-group col-md-4 mb-0'),
                    Column('middle_name',
                           css_class='form-group col-md-4 mb-0'),
                    Column('last_name',
                           css_class='form-group col-md-4 mb-0'),
                    Column('initials',
                           css_class='form-group col-md-4 mb-0'),
                ))