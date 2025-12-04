from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms


def profile_view(request):
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    form = forms.ProfileForm(instance=request.user.profile)
    
    if request.method == "POST":
        form = forms.ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'users/profile_edit.html', {"form": form})