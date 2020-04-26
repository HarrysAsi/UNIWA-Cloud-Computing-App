from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth import authenticate, login, logout

from apps.subject.models import Subject
from apps.user.models import CustomUser


def index_view(request):
    """
    Redirect to the login page of the event management panel
    """
    return redirect("main")


@login_required(login_url="login")
def main_view(request):
    subjects = Subject.objects.all().order_by("date_created")
    context = {
        "subjects": subjects,
    }
    return render(request, 'cloud/main.html', context)


@login_required(login_url="login")
def login_view(request):
    """
    Login to the management platform
    """

    # Redirect to main page if user is authenticated
    if request.user.is_authenticated:
        return redirect("main")

    if request.method == 'POST':
        # form submitted
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        # Check if password and email fields does not exists
        if email is None or password is None:
            messages.error(request, message="Email or password is empty")
        else:
            # Find user
            user = CustomUser.objects.filter(email=email)
            if user:
                # Authenticate user if exists
                auth_user = authenticate(email=email, password=password)
                if auth_user is not None:
                    if auth_user.is_superuser is not True:
                        # If is super user
                        messages.error(request, message="The requested user has not admin privileges")
                        return redirect("login")
                    else:
                        # Creates session
                        login(request, auth_user)
                        return redirect("main")
                else:
                    messages.error(request, message="Invalid Credentials, please try again")
            else:
                messages.error(request, message="Invalid Credentials, please try again")
    return render(request, 'cloud/login.html', {})


def logout_view(request):
    """
    Logout view for the management platform
    """
    logout(request)
    return redirect("login")


def handler404(request, exception):
    return render(request, 'handlers/404.html', status=404)


def handler500(request):
    return render(request, 'handlers/500.html', status=500)
