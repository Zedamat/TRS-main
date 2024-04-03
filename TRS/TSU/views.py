from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm,UpdateRecordForm,NationalityForm, ProductForm, SexForm, PurposeForm
from django.contrib.auth.decorators import login_required
from .models import Nation, Product, Record, Sex, Purpose
from django.core.paginator import Paginator

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# - Homepage 

def home(request):

    return render(request, 'TSU/index.html')


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'You have create account succesfully!')
            return redirect("my-login")

    context = {'form':form}

    return render(request, 'TSU/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request,'You have login succesfully!')
                return redirect("dashboard")
            else:
                messages.success(request,"We couldn't find an account with that username. Try another, or get a new  account.") 
            

    context = {'form':form}

    return render(request, 'TSU/my-login.html', context=context)

# - Dashboard

@login_required(login_url='my-login')

def dashboard(request):

    my_records = Record.objects.all().order_by('-creation_date')
    
    context = {'records':my_records}

    return render(request, 'TSU/dashboard.html', context=context)

# - Create a record 

@login_required(login_url='my-login')

def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            messages.success(request, "Your record was created!")
            return redirect("dashboard")
        else:
            messages.success(request, "Your record not created!")
            

    context = {'form': form}

    return render(request, 'TSU/create-record.html', context=context)

# - Update a record 

@login_required(login_url='my-login')

def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, request.FILES, instance=record)

        if form.is_valid():

            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")
        else:
            messages.success(request, "Your record is not updated!")
        
    context = {'form':form}

    return render(request, 'TSU/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'TSU/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")

# - User logout

def user_logout(request):

    auth.logout(request)

    return redirect("my-login")
def hotel(request):
    products = Product.objects.all().values()
    if request.method == 'POST':
       form2 = ProductForm (request.POST)
       if form2.is_valid():
          form2.save()
          return redirect('hotel')
    else:
        form2 = ProductForm()        

    context = {
        "products": products,
        "form2": form2
    }

    return render(request,'TSU/hotel.html', context=context)

def nation(request):
   
    nations = Nation.objects.all().values()

    if request.method == 'POST':
        form2 = NationalityForm (request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('nation')
    else:
        form2 = NationalityForm()        

    context = {
        "nations": nations,
        "form2": form2
    }

    return render(request, 'TSU/nation.html', context=context)

def sex(request):
   
    sexs = Sex.objects.all().values()

    if request.method == 'POST':
        form3 = SexForm (request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('sex')
    else:
        form3 = SexForm()        

    context = {
        "sexs": sexs,
        "form3": form3
    }

    return render(request, 'TSU/sex.html', context=context)

def purpose(request):

    Purposes = Purpose.objects.all().values()

    if request.method == 'POST':
        form4 = PurposeForm (request.POST)
        if form4.is_valid(): 
            form4.save()
            return redirect('purpose')
    else:
        form4 = PurposeForm()        

    context = {
        "Purposes": Purposes,
        "form4": form4
    }

    return render(request, 'TSU/purpose.html', context=context)
# Change_Password
