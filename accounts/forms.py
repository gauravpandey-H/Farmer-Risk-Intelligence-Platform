from django import forms
from django.contrib.auth.models import User
from farmers.models import Farmer

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # Farmer fields
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    village = forms.CharField(max_length=100, required=True)
    district = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    land_size = forms.DecimalField(max_digits=6, decimal_places=2, required=True, help_text="In acres")

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'] # using email as username
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Farmer.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                phone=self.cleaned_data['phone'],
                email=self.cleaned_data['email'],
                village=self.cleaned_data['village'],
                district=self.cleaned_data['district'],
                state=self.cleaned_data['state'],
                land_size=self.cleaned_data['land_size']
            )
        return user
