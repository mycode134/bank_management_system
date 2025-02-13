from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

def add_cus(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_cus')
    else:
        form = CustomerForm()
    return render(request, 'add_cus.html', {'form': form})


def edit_cus(request, cus_id):
    customer = get_object_or_404(Customer, id=cus_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('view_all_cus')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_cus.html', {'form': form})
    
def view_all_cus(request):
    customers=Customer.objects.all()
    return render(request, 'view_all_cus.html',{'customers':customers})   

def delete_cus(request,cus_id):
    customers=get_object_or_404(Customer,id=cus_id)
    customers.delete()
    return redirect('view_all_cus')

def filter_cus(request):
    account_no = request.GET.get('account_no')
    customers = Customer.objects.filter(account_no=account_no) if account_no else []
    return render(request, 'filter_cus.html', {'customers': customers})

def transfer_money(request):
    if request.method == 'POST':
        sender_account_no = request.POST.get('sender_account_no')
        receiver_account_no = request.POST.get('receiver_account_no')
        amount = float(request.POST.get('amount'))

        if sender_account_no == receiver_account_no:
            messages.error(request, "Sender and receiver accounts cannot be the same.")
            return redirect('transfer_money')

        sender = get_object_or_404(Customer, account_no=sender_account_no)
        receiver = get_object_or_404(Customer, account_no=receiver_account_no)

        if sender.balance < amount:
            messages.error(request, "Insufficient funds in sender's account.")
            return redirect('transfer_money')

        sender.balance -= amount
        receiver.balance += amount
        sender.save()
        receiver.save()

        messages.success(request, "Transaction successful.")
        return redirect('view_all_cus')
    return render(request, 'transfer_money.html')




