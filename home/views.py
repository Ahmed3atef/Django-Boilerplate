from django.shortcuts import redirect, render
from .tasks import notify_customers

def home_view(request):
    return render(request, 'index.html')


def send_emails(request):
    notify_customers.delay('Hello World!')
    return redirect("home")