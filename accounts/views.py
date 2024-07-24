from django.contrib.auth import get_user_model, login
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import UserRegisterForm, UserLoginForm

User = get_user_model()


@transaction.atomic()
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            phone_number = user_data.pop('phone_number')
            if not User.objects.filter(phone_number=phone_number):
                User.objects.create_user(
                    phone_number=phone_number
                )

            return redirect(reverse('accounts:login'))
    return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user_data = form.cleaned_data
            try:
                user = User.objects.get(phone_number=user_data['phone_number'])
            except User.DoesNotExist:
                user = None

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
    return render(request, "accounts/login.html")
