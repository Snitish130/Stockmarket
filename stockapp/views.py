from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from stockapp.forms import StockForm
from stockapp.models import StockList
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse 
import xlwt

@login_required(login_url='login')
def home(request): # this is the homepage of stock market
    if request.user.is_authenticated:
        form = StockForm()
        stocks = StockList.objects.all()
        return render(request , 'index.html' , context = {'form':form , 'stocks':stocks})

def stockDetail(request , slug): # this method show the details of stock  
    stock = StockList.objects.get(slug=slug)
    return render(request , 'stockdetail.html' , context = {'stock':stock})


def searchstock(request): # this method fetch the data of particular stock 
    if request.user.is_authenticated:
        form = StockForm()
        search = request.POST.get('name')
        stocks = StockList.objects.filter(name__contains=search)
        return render(request , 'index.html' , context = {'form':form , 'stocks':stocks})


def login(request): # this method loging the user
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request , 'login.html' , context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid(): # form validation
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            print("Authenticated " , user)
            if user is not None:
                loginUser(request , user)
            return redirect('home')
        else:
            return render(request , 'login.html' , context=context)

@login_required(login_url='login')
def signup(request): # this method create the account of new user
    if request.method=='GET':
        form = UserCreationForm()
        context = { 
            'form' : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        
        form = UserCreationForm(request.POST)
        context = {
            'form' : form
            }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)

def signout(request): # this method logout the user
    logout(request)
    return redirect('login')

def add_stock(request): # this method add new stock in the list
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = user
            stock.save()
            print(stock)
            return redirect('home')
        else:
            return render(request , 'index.html' , context = {'form':form})

def export_data_xls(request ,slug): # this method export the particular stock data
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Stock Data') # this will make a sheet named Stock Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'industry', 'description', 'mcap', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = StockList.objects.filter(slug=slug).values_list('name', 'industry', 'description', 'mcap')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response