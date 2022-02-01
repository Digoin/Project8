from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model

from .forms import SignUpForm

User = get_user_model()


def signup(request):
    """Show the signup page to let the user create an account."""

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect("main_site:home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
