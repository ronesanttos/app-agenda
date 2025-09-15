from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from contact.form import RegisterForm, UpdateForm
from django.contrib.auth.decorators import login_required


def register(req):
    form = RegisterForm()

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        
        if form.is_valid():
            form.save()
            messages.success(req, "Cadastrado com sucesso!")
            return redirect("contact:index")
        
        else:
            messages.error(req,'Erro ao criar o contato.')
    return render(
        req,
        'contact/register.html',
       {
           'form': form,
        }
    )
    
def login(req):
    form = AuthenticationForm(req)
    
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(req,user)
            messages.success(req, 'Login feito com sucesso!')
            return redirect('contact:index')
        messages.error(req, 'Login invalido')
        
    return render(
        req,
        'contact/login.html',
       {
           'form': form,
        }
    )
    

@login_required(login_url='contact:login')
def update(req):
    form = UpdateForm(instance=req.user)
    
    if req.method == 'POST':
        form = UpdateForm(req.POST, instance=req.user)
        
        if form.is_valid():
            form.save()
            return redirect('contact:update')
     
    return render(
        req,
        'contact/update.html',
       {
           'form': form,
        }
    )

@login_required(login_url='contact:login')
def logout(req):
    auth.logout(req)
    return redirect('contact:update')