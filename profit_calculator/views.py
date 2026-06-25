from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profit
from .forms import ProfitForm

@login_required
def profit_dashboard(request):
    if hasattr(request.user, 'farmer'):
        profits = Profit.objects.filter(crop__farmer=request.user.farmer)
    else:
        profits = []
        
    return render(request, 'profit_calculator/dashboard.html', {'profits': profits})

@login_required
def add_profit_estimate(request):
    if request.method == 'POST':
        form = ProfitForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profit estimate calculated and saved successfully!")
            return redirect('profit_dashboard')
    else:
        form = ProfitForm(user=request.user)
        
    return render(request, 'profit_calculator/add_estimate.html', {'form': form})
