from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Re-enter password",
        widget=forms.PasswordInput
        )
    password = forms.CharField(
        widget=forms.PasswordInput
        )
    username = forms.CharField(
        help_text="case sensitive",
    )
    phone = forms.CharField(
        help_text=" ",
    ) 
    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name', 'last_name', 'phone', 'password', )
    
    
    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        p = data['password2']
        p_1 = data['password']
        if len(p) < 6:
            raise forms.ValidationError('Your password should be 6 or more characters')
        if p == p_1:
            return p
        raise forms.ValidationError("Your passwords do not match")