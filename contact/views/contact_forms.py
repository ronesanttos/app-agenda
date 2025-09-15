from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from contact.models import Contact
from contact.form import ContactForm

@login_required(login_url='contact:login')
def create(req):
    form_action = reverse('contact:create')

    if req.method == 'POST':
        form = ContactForm(req.POST, req.FILES)
        
        context = {
           'form': form,
           'form_action': form_action
       }
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = req.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
        req,
        'contact/create.html',
         context
        )
       
    context = {
      'form': ContactForm(),
      'form_action' : form_action,
    }
    
    return render(
        req,
        'contact/create.html',
        context
    )
    
    
@login_required(login_url='contact:login')
def update_contact(req, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=req.user)
    
    form_action = reverse('contact:update', args={contact_id,})

    if req.method == 'POST':
        form = ContactForm(req.POST, req.FILES, instance=contact)
        
        context = {
           'form': form,
           'form_action': form_action,
       }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update',contact_id= contact.pk)
        
        return render(
        req,
        'contact/create.html',
        context
        )
       
    context = {
      'form': ContactForm(instance=contact),
      'form_action' : form_action,
    }
    
    return render(
        req,
        'contact/create.html',
        context
        
    )
    

@login_required(login_url='contact:login')
def delete(req, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True,owner=req.user)
    
    confirmation = req.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        req,
        'contact/contact.html',
        {
        'contact': contact,
         'confirmation':confirmation,
      }
    )