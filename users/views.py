from django.shortcuts import redirect, render 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


# the register view when a user wants to register 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('Post')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        print('get')
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    query = Profile.objects.all()
    u_form = UserUpdateForm() 
    p_form = ProfileUpdateForm()

    print(query)
    
    result = {
        'profile': query,
        'u_form': u_form,
        'p_form': p_form,
        }
    return render(request,'users/profile.html',result)


def update_Profile(request):
    return render(request,'users/update_profile.html')