from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm


#pour notre classe UserRegistration.Nous avons l'intention d'inclure un mot de passe et de confirmer le champ de mot de passe dans ce formulaire en correspondance avec nos attributs de modèle d'utilisateur 
#Dans la classe UserRegistration nous avons une méthode de validation personnalisée affichée avec le clean_password2 qui garantit simplement que les deux mots de passe correspondent sinon cela génère une erreur de validation .
   
class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


