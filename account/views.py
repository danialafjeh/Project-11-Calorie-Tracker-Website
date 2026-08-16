from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserBody
from main.models import DailyReport, FoodIntake
from .forms import SignUpForm, SignInForm, UpdateUserForm, UpdateUserPasswordForm, UpdateUserBodyForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserBody.objects.create(
                user=user,
                age=form.cleaned_data['age'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                gender=form.cleaned_data['gender'],
                physical_activity=form.cleaned_data['physical_activity']
            )

            auth_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            login(request, auth_user)
            messages.success(request, ("Your account has been created successfully."))
            return redirect('home_page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

                return redirect('signup_page')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                if not auth_user.is_staff:
                    login(request, auth_user)
                    messages.success(request, ('You signed in to your account.'))
                    return redirect('home_page')
                else:
                    messages.error(request, ('Sorry, this account has admin permissions.'))
                    return redirect('signin_page')
            else:
                messages.error(request, ('Sorry, username or password was wrong.'))
                return redirect('signin_page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            
                return redirect('signin_page')
    else:
        form = SignInForm()
        return render(request, 'signin.html', {'form':form})



def signin_for_admin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                if auth_user.is_staff:
                    login(request, auth_user)
                    messages.success(request, ('You signed in to your admin account.'))
                    return redirect('home_page')
                else:
                    messages.error(request, ('Sorry, this account does not have admin permissions.'))
                    return redirect('signin_admin_page')
            else:
                messages.error(request, ('Sorry, username or password was wrong.'))
                return redirect('signin_admin_page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            
                return redirect('signin_admin_page')
    else:
        form = SignInForm()
        return render(request, 'signin_admin.html', {'form':form})
    
    

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, ('You signed out of your account.'))
        return redirect('home_page')
    else:
        messages.error(request, ('Sorry, something went wrong.'))
        redirect('home_page')



def profile(request):
    if request.user.is_authenticated:
        account_info = get_object_or_404(User, id=request.user.id)
        body_info = get_object_or_404(UserBody, user__id=request.user.id)
        reports_info = DailyReport.objects.filter(user__id=request.user.id)

        info = {
            'acc_info':account_info,
            'body_info':body_info,
            'reports_info':reports_info
        }
        return render(request, 'profile.html', info)
    else:
        messages.error(request, ('You must be signed in to an account to access your profile.'))
        return redirect('home_page')



def update_acc_info(request):
    if request.user.is_authenticated:
        current_info = get_object_or_404(User, id=request.user.id)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance = current_info)
            if form.is_valid():
                form.save()
                messages.success(request, ('Your information has been updated.'))
                return redirect('profile_page')
            else:
                messages.error(request, ('Sorry, something went wrong'))
                return redirect('update_acc_info')
        else:
            form = UpdateUserForm(instance = current_info)
            return render(request, 'update_acc_info.html', {'form':form})
    else:
        messages.error(request,('You must be signed in to an account to access this page.'))
        return redirect('home_page')



def update_acc_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method =='POST':
            form = UpdateUserPasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,('Your password has been updated.'))
                login(request, current_user)
                return redirect('profile_page')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)

                    return redirect('update_acc_password')
        else:
            form = UpdateUserPasswordForm(current_user)
            return render(request,'update_acc_pass.html',{'form':form})
    else:
        messages.error(request,('You must be signed in to an account to access this page.'))
        return redirect('home_page')



def update_body_info(request):
    if request.user.is_authenticated:
        current_info = get_object_or_404(UserBody, user__id=request.user.id)
        if request.method == 'POST':
            form = UpdateUserBodyForm(request.POST, instance = current_info)
            if form.is_valid():
                form.save()
                messages.success(request, ('Your information has been updated.'))
                return redirect('profile_page')
            else:
                messages.error(request, ('Sorry, something went wrong'))
                return redirect('update_body_info')
        else:
            form = UpdateUserBodyForm(instance = current_info)
            return render(request, 'update_bodyinfo.html', {'form':form})
    else:
        messages.error(request,('You must be signed in to an account to access this page.'))
        return redirect('home_page')



def view_reports_details(request, id):
    if request.user.is_authenticated:
        report = get_object_or_404(DailyReport, id=id)
        related_food_intake = FoodIntake.objects.filter(report=report)

        info = {
            'report':report,
            'food_intake':related_food_intake
        }
        return render(request, 'reports_details.html', info)
    else:
        messages.error(request,('You must be signed in to an account to access this page.'))
        return redirect('home_page')
    