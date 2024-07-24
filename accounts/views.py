from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import UserRegisterForm

User = get_user_model()


@transaction.atomic()
def authorize_user(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user_data = form.cleaned_data
            phone_number = user_data.pop('phone_number')
            if not User.objects.filter(phone_number=phone_number):
                User.objects.create_user(
                    phone_number=phone_number
                )

            return redirect(reverse('index'))
    return render(request, 'accounts/authorize.html')
