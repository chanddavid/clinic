from django import forms
from .models import User,Role
class UserForm(forms.ModelForm):
    is_superuser = forms.BooleanField(initial=False,
                                      widget=forms.RadioSelect(choices=[(True, 'Yes'),
                                                            (False, 'No')],
                                         ))

    is_active = forms.BooleanField(initial=False,
                                      widget=forms.RadioSelect(choices=[(True, 'Yes'),
                                                                        (False, 'No')],
                                                               ))
#     ROLE_CHOICES =(
#     ("Doctor", "Doctor"),
#     ("Admin", "Admin"),
#     ("Lab", "Lab"),
#     ("Accountant", "Accountant"),
#     ("OPD", "OPD"),
# )
#     role=forms.ChoiceField(choices=ROLE_CHOICES)
    class Meta:
        model = User
        fields = "__all__"


class RoleForm(forms.Form):
    class Meta:
        model=Role
        fields="__all__"


