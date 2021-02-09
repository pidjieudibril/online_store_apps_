from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


# Create your views here.
#def dashboard (): Cette fonction contient un décorateur de connexion le rendant accessible uniquement lorsque l'utilisateur est connecté, qui rend ensuite le texte «Bienvenue dans votre tableau de bord» à l'utilisateur.
@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your "
    }
    return render(request, 'store/index.html', context=context)

def dashboard1(request):
    context = {
        "welcome": "Welcome to your profile "
    }
    return render(request, 'authapp/dashboard1.html', context=context)


#Cette fonction est responsable de l'enregistrement d'un nouvel utilisateur dans notre application et utilise la classe UserRegistration que nous avons créée dans notre forms.py 
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)#form.save (commit = False) car nous devons modifier les données avant de les enregistrer dans la base de données
           #pour hacher le nouveau mot de passe utilisateur en utilisant new_user.set_password ()
            new_user.set_password( 
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)
