# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CoustomUser

# class CoustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CoustomUser
#         fields = tuple(UserCreationForm.Meta.fields) if isinstance(UserCreationForm.Meta.fields, (list, tuple)) else ('username', 'password1', 'password2')
#         fields += ('age', 'address', 'zip', 'phone',)

# class CoustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CoustomUser
#         fields = tuple(UserCreationForm.Meta.fields) if isinstance(UserCreationForm.Meta.fields, (list, tuple)) else ('username', 'password1', 'password2')
#         fields += ('age', 'address', 'zip', 'phone',)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CoustomUser

class CoustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CoustomUser
        fields = tuple(UserCreationForm.Meta.fields) if isinstance(UserCreationForm.Meta.fields, (list, tuple)) else ('username', 'password1', 'password2')
        fields += ('age', 'address', 'zip', 'phone',)

class CoustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CoustomUser
        fields = ('username', 'email', 'age', 'address', 'zip', 'phone',)
