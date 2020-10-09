from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import TutorRegisterForm, ProfileUpdateForm, UserUpdateForm
from.models import profile


#home page 
def home(request):
	return render(request, 'tutors/home.html')


#find tutors
def find(request):
	content = {
	     'profile':profile.objects.all()
	}
	return render(request, 'tutors/find.html', content)



# User creation view

def register(request):
	if request.method == 'POST':
		form = TutorRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created you can  now login')
			return redirect('login')

	form = TutorRegisterForm()
	return render(request, 'tutors/register.html', {'form': form})
	
#user profile	
@login_required
def profile(request):
	u_form = UserUpdateForm()
	p_form = ProfileUpdateForm()

	context = {
	    'u_form': u_form,
	    'p_form': p_form

	}
    

	return render(request, 'tutors/tutor_profile.html',context)
		
	
