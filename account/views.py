from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup_view(request):

    # return HttpResponse("home")
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        #user loggedin
        return redirect('articles:list')
    else:  
       form = UserCreationForm() 
    return render(request,'signup.html',{'form':form})