from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from .form import UserRegistrationForm

#def admin_app(request):
#    template = loader.get_template('firstpage.html')
#    return HttpResponse(template.render)

def admin_app(request):
   return render(request, 'firstpage.html')

def register_member(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)


            user.save()
            return redirect('sucess')  # Redirect to the login page after successful registration
    else:
       # form = UserRegistrationForm()
    #return render(request, 'register.html', {'form': form})
     return redirect('failure')