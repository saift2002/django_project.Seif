from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
import datetime

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        man = authenticate(request, username=username, password=password)
        if man is not None:
            login(request, man)
            return redirect('mainPage')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request , 'index.html')

def mainPage(request):
    fawry = Fawry.objects.all()
    total = user.objects.all()

    context = {
        'money': total,
        'fawry': fawry
    }

    return render(request , 'store.html' , context)

def details(request , obj_id):
    fawzy = Fawry.objects.get(id = obj_id)
    transc = Transaction.objects.filter(fawry = fawzy)
    context={
        'transaction':transc,
        'fawry': fawzy
    }

    return render(request , 'page-1.html' , context)

def update_expenses(request):
    fawry = Fawry.objects.all()
    total = user.objects.all()
    context = {
        'money': total,
        'fawry': fawry
    }
    if request.method == 'POST':
        if 'button1' in request.POST:
            money = request.POST['money']
            User, created = user.objects.get_or_create(pk=1)
            User.total_money += int(money)
            User.save()
            return redirect('mainPage')
        elif 'button2' in request.POST:
            money = request.POST['money']
            User, created = user.objects.get_or_create(pk=1)
            User.total_money = int(money)
            User.save()
            return redirect('mainPage')
    return render(request, 'store.html', context)

def add_transaction(request, obj_id):
    dateee = datetime.datetime.now().date()
    if request.method == 'POST':
        type = request.POST["payment_type"]
        amount = request.POST['amount']
        amount1 = request.POST['amount1']
        obj = get_object_or_404(user, pk=1)
        obj.total_money -= int(amount)
        if obj.total_money<0:
            messages.success(request, 'what the fuck man shit!!!') 
            return redirect('mainPage')
        obj.save()
        fwaryy = get_object_or_404(Fawry , id= obj_id)
        if (fwaryy.money_borrowed + int(amount)) - (fwaryy.money_payed_back + int(amount1))<0:
            return redirect('mainPage')
        fwaryy.money_borrowed += int(amount)
        fwaryy.money_payed_back += int(amount1)
        fwaryy.difference = fwaryy.money_borrowed - fwaryy.money_payed_back

        fwaryy.save()
        # Create a new Transaction object
        transaction = Transaction.objects.create(
            fawry=fwaryy,
            date = str(dateee),
            amount_spent=amount,
            amount_received=amount1,
            profit = type,
        )
        transaction.save()
        
        return redirect('mainPage') 
    
    # Handle the case when the method is not POST (optional)
    return redirect('mainPage')
