from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .EmailForm import EmailForm
from .models import Student   

def home(request):
    return render(request,'app1/home.html')

def students(request):
    students = Student.objects.all()   
    return render(request, 'app1/students.html', {"students":students})

def colleges(request):
    return render(request, 'app1/colleges.html')

def address(request):
    return render(request, 'app1/address.html')

def boot(request):
    return render(request,'app1/boot.html')

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['24b01a1217@svecw.edu.in'], 
                fail_silently=False,
            )
            return render(request, 'app1/success.html')
    else:
        form = EmailForm()

    return render(request, 'app1/submit.html', {'form': form})