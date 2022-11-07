from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Project, Skills


# mail function
def mail_send(message, template, to_mail):
    email = EmailMessage(message, template, settings.EMAIL_HOST_USER, [to_mail])
    email.fail_silently = False
    email.send()


# Create your views here.
def index(request):

    objects = Project.objects.all()
    skills_data = Skills.objects.all()
    context = {'objects':objects, 'skills':skills_data}
    


    if request.method == 'POST':

        name = request.POST['name']
        reply_to = request.POST['email']
        message = request.POST['msg']
        # print(name, reply_to, message)
        template = render_to_string('mail_template.html', {'name': name})
        template_admin = render_to_string('mail_template_for_admin.html', {'name': name, 'email':reply_to, 'message':message})

        mail_send('Thanking For Contect Mail', template, reply_to)
        mail_send('Contect Mail', template_admin, 'mohankumarmk058@gmail.com')

        return render(request, 'index.html', context=context)


    return render(request, 'index.html', context=context)



# def example(request):
#     objects = Project.objects.all()
#     context = {'objects': objects}

#     return render(request, 'example.html', context)



