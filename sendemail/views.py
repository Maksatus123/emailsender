from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from config.settings import EMAIL_RECIPIENTS, DEFAULT_FROM_EMAIL

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message, DEFAULT_FROM_EMAIL, EMAIL_RECIPIENTS)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'email.html', {'form':form})


def success_view(request):
    return HttpResponse("Приняли! Спасибо за заявку")
