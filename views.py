from django.shortcuts import HttpResponse,redirect,render
import pandas as pd 
import streamlit as st 
import pandas as pd 
import os
import plotly.figure_factory as ff
import warnings
import plotly.express as px
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoTokenizer , AutoModelForCausalLM
# from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate,login
warnings.filterwarnings('ignore')
# from .models import CustomerForm

# def customer_registration(request):
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')  # Redirect to a success page or another view
#     else:
#         form = CustomerForm()
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Custom redirect logic
            if user.is_superuser:
                return redirect('admin:index')  # Example redirect for admin users
            return render(request,'index.html') # Redirect to a specific page for regular users
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def generater_page(request):
    return render(request, 'GPT.html')
def homepage(request):
    return render(request , 'index.html')
def Waste_FAQ(request): 
    return render(request , 'FAQ.html')
def Waste_Schedule(request):
    return render(request,'schedule.html')
def sanitation_report(request):
    return render(request,'report.html')
def facts(request):
    return render(request , 'fact.html')
def Recycling_guide(request):
    return render(request , 'guide.html')
def waste_dashBoard(request):
    return render(request , "Waste_DashBoard.html")
def Waste_Quiz(request):
    return render(request,'Quiz.html')
def chat_view(request):
    return render(request , 'GPT.html')