from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
 
def signup(request):
 
    if request.user.is_authenticated:
        return redirect('/dashboard')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/')
         
        else:
            return render(request,'users/signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'user/signup.html',{'form':form})
 
 
def signin(request):
    if request.user.is_authenticated:
        return redirect('/dashnoard')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            form = AuthenticationForm()
            return render(request,'users/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'users/signin.html', {'form':form})
 
 
def signout(request):
    logout(request)
    return redirect('/signin/')