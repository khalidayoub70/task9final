from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from .models import Intern
from .forms import PizzaForm, MultiplePizzaForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.forms import formset_factory

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform':new_form, 'note':note, 'multiple_form':multiple_form, })
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'multiple_form':multiple_form, 'pizzaform':form})

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset':formset})





def submit_work(request):
    interns = Intern.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or display a success message
            return HttpResponseRedirect('/success/')
    else:
        form = TaskForm()
        print('internlist',interns)
    
    return render(request, 'home.html', {'form': form, 'interns': interns})
def Success(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'success.html')
def superadmin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, password=password)
        my_user.save()
        print(uname, password)
        return redirect('admin1')

    return render(request,'pizza/superadmin.html')
def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request,user)
            return redirect('authorized')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'pizza/admin1.html')

def admin1(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request,user)
            return redirect('authorized')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'pizza/admin1.html')


#def accounts(request):
#    return render(request, 'welcome.html',{'today': datetime.today()})

@login_required(login_url='/login')
def authorized(request):
    return render(request, 'pizza/authorized.html',{})

def dummy(request):
    data={
        'clist':['a','b','c','d','e','f','g','h','i','j']
    }
    return render(request,'dummy.html',data)