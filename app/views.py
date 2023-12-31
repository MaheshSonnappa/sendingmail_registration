from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def registration(request):
    usfo = UserForm()
    pfo = ProfileForm()
    d = {"usfo": usfo, "pfo": pfo}
    if(request.method == 'POST' and request.FILES):
        usfd = UserForm(request.POST)
        pfd = ProfileForm(request.POST, request.FILES)
        if(usfd.is_valid() and pfd.is_valid()):
            NSUFO = usfd.save(commit=False)
            sentData = usfd.cleaned_data['password']
            NSUFO.set_password(sentData)
            NSUFO.save()
            NSPO = pfd.save(commit=False)
            NSPO.username = NSUFO
            NSPO.save()
            send_mail('Registration', 'Your registration is successfully Done', 'mm2044488@gmail.com', [NSUFO.email], fail_silently=False)
            return HttpResponse("<marquee><h1>registered successfully</h1></marquee>")
    return render(request, "registration.html", d)
