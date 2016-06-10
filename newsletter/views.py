from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import SignUpForm, ContactForm
from .models import SignUp


# Requests are what you request from the server. The server return something back.
def home(request):
    title = "Welcome"
    # request.POST runs through the validators, if there's no data it doesnt run through it
    # if request.POST is true (in this case if you press the button), use the POST information in the validators,
    # if its false, don't use any info(which means that it will not run through the validators)
    # the POST info, here, is the full_name and the email
    form = SignUpForm(request.POST or None)
    context = {
        "template_title": title,
        "form": form,
    }

    # checks if the given data is valid, if the model is valid, like making sure the name is/not blank, etc
    if form.is_valid():
        # sets variable but doesnt save it. allows us to do something before saving
        instance = form.save(commit=False)
        # sets variable 'full_name' to be the full_name data from the form
        full_name = form.cleaned_data.get("full_name")
        # if its empty, sets the var above^ to the string, else leave as given
        if not full_name:
            full_name = "New Full Name"
        # sets the full_name from the form to the full_name var.
        instance.full_name = full_name
        instance.save()
        # after completing the forms, change the context
        context = {
            "template_title": "Success, " + instance.full_name,
        }
    if request.user.is_authenticated() and request.user.is_staff:
        # print(SignUp.objects.all().all())
        # for instance in SignUp.objects.all():
        #    print(instance.full_name)
        queryset = SignUp.objects.all().order_by('-timestamp')
        #.filter(full_name__icontains="Caio Camatta")
        context = {
            "queryset": queryset,
        }

    return render(request, "newsletter/home.html", context)


def contact(request):
    title = "Contact us"
    form = ContactForm(request.POST or None)
    text_centered = True
    if form.is_valid():
        # because form.cleaned_data is a dict, we can do this
        # for key, value in form.cleaned_data.items():
        #     # key = "email", value = "caiocamattacoelho@hotmail.com"
        #     print(key, value)

        # cleaned_data means that its just the data in a clean way
        print(form.cleaned_data)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        """ Send email """
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'anotheremail@email.com']
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)
        some_html_message="<p>Hello<p>"
        # after defining the info, use it to send email
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  html_message=some_html_message,
                  fail_silently=True)


    context = {
        "form": form,
        "title": title,
        "text_centered": text_centered,
    }
    return render(request, "newsletter/forms.html", context)


def about(request):
    return render(request, 'newsletter/home.html', {})


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
