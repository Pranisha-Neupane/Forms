from django.shortcuts import render

def Homepage(request):
    return render(request, 'Home.html')

def LoginPage(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(request, email=email, password=password)
    #     print(email, password)
    #     return redirect('home')
    return render(request, 'Login.html')

def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')  
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(uname, email, pass1,pass2)  
        return render(request, 'SignUp.html')  # Response for POST requests

    return render(request, 'SignUp.html')
