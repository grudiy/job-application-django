from django.shortcuts import render
from forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Create object in Model (store data in database table)
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            message_body = f"Hi {first_name} {last_name}. Your job application form was submitted."
            email_message = EmailMessage("Form submission confirmation(django)", message_body, to=[email, 'gruand@gmail.com'])
            email_message.send()

            messages.success(request, "Form submitted successfully!")

    return render(request, "index.html")
