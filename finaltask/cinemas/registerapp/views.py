from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from registerapp.models import UserProfile
from .forms import UserProfileForm

# Create your views here.
@login_required
def view_profile(request):
    try:
        user_profile = request.user.userprofile
    except ObjectDoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('registerapp:view_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'view_profile.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('movieapp:movie')

        else:
            messages.info(request, "invalid credentials")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return render(request, "index.html")


def sign_in(request):
    if request.method == 'POST':
        userid = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['passwrd']
        confirm_password = request.POST['cnfpasswrd']
        email = request.POST['email']
        if User.objects.filter(username=userid).exists():
            messages.error(request, "Username is already taken. Please choose another one.")
            return redirect('registerapp:sign_in')
            # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address is already in use.")
            return redirect('registerapp:sign_in')
            # Create the user
        user = User.objects.create_user(username=userid, first_name=first_name, last_name=last_name,
                                        password=password, email=email)

        # user_profile, created = UserProfile.objects.get_or_create(user=user)
        # user_profile.first_name = first_name
        # user_profile.last_name = last_name
        # user_profile.email = email
        # user_profile.save()
        messages.success(request, "User created successfully. Welcome to Cineworld!")
        return redirect('registerapp:login')

        # If the request method is not POST, render the sign-in form

    return render(request, 'sign_in.html')



# @login_required
# def edit_profile(request):
#
#     user_profile = request.user.userprofile  # Assuming userprofile is related name in the UserProfile model
#     form = UserProfileForm(request.POST or None, request.FILES,instance=user_profile)
#     if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('edit_profile')
#     return render(request, 'edit_profile.html', {'form': form})
