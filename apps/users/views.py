from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.
def loging(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        return redirect('/login.html')
    elif request.method == 'GET':
        return render(request,'login.html',{ })
        