from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def home(request):
    username = request.session.get('username')
    password = request.session.get('password')

    user_info = {
        "username":username,
        "password":password,
    }
    return render(request,'ecommerce/home.html',user_info)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pw = request.POST.get('pass')

        # validating the data from database and storing in the session.
        if User.objects.filter(username = uname,password = pw).exists():
            request.session['username'] = uname
            request.session['password'] = pw

            return redirect('home')
        else:
            return render(request,'ecommerce/login.html',{
                "error_msg":"Details didn't matched.",
                })
        
    return render(request,'ecommerce/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        confirm_pass = request.POST.get('cpass')

        # Storing the data into the database
        if password == confirm_pass:
            User.objects.create(username = username,password = password)
            return redirect('login')
        else:
            return render(request,'ecommerce/signup.html',{
                "error_msg":"Details didnot matched",
            })

    return render(request,'ecommerce/signup.html')

def logout(request):
    request.session.flush()
    return redirect('login')