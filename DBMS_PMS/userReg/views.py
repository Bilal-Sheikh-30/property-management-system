from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser  # Assuming your model is in the same app
from dashboard import views
from django.contrib import messages
def home(request):
  return render(request,'home.html')

def signup(request):
  if request.method == 'POST':
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone')
    cnic = request.POST.get('cnic')

    # Validate data (optional)
    input_status = 'pass'

    # chk if cnic and phone num are numbers
    if cnic.isnumeric() != True:
      input_status = 'invalid'
      messages.error(request, 'This CNIC is invalid.')
    elif phone_number.isnumeric() != True:
      input_status = 'invalid'
      messages.error(request, 'This Phone No is invalid.')

    # chk if cnic alreagy exists
    if CustomUser.objects.filter(cnic=cnic).exists():
      input_status = 'invalid'
      messages.error(request, 'This CNIC is already registered.')
    elif CustomUser.objects.filter(email=email).exists():
      input_status = 'invalid'
      messages.error(request, 'This email is already registered.')
    elif CustomUser.objects.filter(phone_number=phone_number).exists():
      input_status = 'invalid'
      messages.error(request, 'This Phone Number is already registered.')

    
    if input_status == 'pass':
      user = CustomUser.objects.create_user(
        username = email,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        cnic=cnic,
        phone_number=phone_number
      )
      if user is not None:
        login(request, user)  # Login the user
        return redirect('property_list')  # Redirect to the home page after successful login
      else:
        # Handle user creation error (e.g., display message)
        messages.error(request,'User creation failed. Please try again.')

    

  return render(request, 'registration/checkregister.html')



def logined(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Authenticate the user based on email (as you're using email as username)
    user = authenticate(email=email, password=password)

    if user is not None:
      login(request, user)  # Login the user if credentials are valid
      return redirect('property_list')  # Redirect to the home page after successful login
    else:
      # Handle unsuccessful login attempt (e.g., display error message)
      messages.error(request,'invalid credentials')

  return render(request, 'registration/checklogin.html')