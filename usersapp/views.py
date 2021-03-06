from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import  UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib  import messages

def register(request):
    if request.method =="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Your Account is created you are noew able to login In !")
            return redirect('usersapp:login')
    else:
        form=UserRegisterForm()
    return render(request,'usersapp/register.html',
                  {'formcntxobj':form})
@login_required
def profile(request):
    if request.method =="POST":
        form_u=UserUpdateForm(request.POST,instance=request.user)
        form_p=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profilemodel)
        if form_p.is_valid() and form_u.is_valid():
            form_p.save()
            form_u.save()
            messages.success(request,f"Your Account is Updated !")
            return redirect('usersapp:profile')
    else:
        form_u=UserUpdateForm(instance=request.user)
        form_p=ProfileUpdateForm(instance=request.user.profilemodel)
    return render(request,'usersapp/profile.html',{ 'form_u':form_u, 'form_p':form_p})

