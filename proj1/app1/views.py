from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from app1.models import Inventory, Req, Temp

flag = None

def loginvalidation(req):
    if req.method == 'POST':

        uname = req.POST['name']
        password = req.POST['password']
        try:
            u = User.objects.get(username=uname)
            if u.check_password(password):
                user = authenticate(username=u, password=password)
                login(req, user)
                if u.is_superuser == True:
                    global flag
                    flag = True
                else:
                    flag = False
                return redirect('/home/')
                
            else:
                return render(req, 'app1/login.html', {'mess': 'user id or pass invalid'})
        except:
            return render(req, 'app1/login.html', {'mess': 'something wrong'})

def login_view(req):
    return render(req, 'app1/login.html')


@login_required
def test(req):
        return render(req, 'app1/test.html',{'mess':flag})

    
    

@login_required
def home(req):
    record = Inventory.objects.values()
    context = {'data':record}
    if flag == True:
        return render(req, 'app1/home_admin.html',context)
    else:
        return render(req, 'app1/home.html',context)

@login_required
def form(req):
    Temp.objects.all().delete()
    return render(req, 'app1/form.html')

@login_required
def inventory(req):
    record = Inventory.objects.values()
    context = {'data':record}
    return render(req, 'app1/inventory.html', context)

@login_required
def inventory2(req):
    record = Req.objects.all().values()
    context = {'data':record}
    return render(req, 'app1/inventory2.html', context)

def about(req):
    return render(req, 'app1/about.html')


@login_required
def submit(req):  
    name=req.GET['name']
    code=req.GET['code']
    item=req.GET['item']
    category=req.GET['category']
    total=req.GET['total']
    stock=req.GET['stock']
    quantity = int(total) - int(stock)
    vendor=req.GET['vendor']
    price=req.GET['price']
    date = req.GET['date']
    des=req.GET['des']
    jus=req.GET['jus']

    rec = Temp.objects.last()
    record = Temp.objects.values()
    context = {'data':record,'name':name}
    if rec:
        if rec.item == item:  
            return render(req, 'app1/requisition.html', context)
    
    u = Temp(faculty = name,
            code = code,
            item = item,
            total = total,
            stock = stock,
            des = des,
            jus = jus,
            category=category,
            quantity =quantity,
            vendor=vendor,
            price=price,
            date=date,)
    
    u.save()
    return render(req, 'app1/requisition.html', context)

@login_required
def form2(req):
    name=req.GET['name']
    code=req.GET['code']
    item=req.GET['item']
    category=req.GET['category']
    total=req.GET['total']
    stock=req.GET['stock']
    quantity = int(total) - int(stock)
    vendor=req.GET['vendor']
    price=req.GET['price']
    date = req.GET['date']
    des=req.GET['des']
    jus=req.GET['jus']

    rec = Temp.objects.last()
    if rec:
        if rec.item == item and rec.code == code and rec.category == category:
            return render(req, 'app1/form2.html',{'name':name})
        
    u = Temp(faculty = name,
            code = code,
            item = item,
            total = total,
            stock = stock,
            des = des,
            jus = jus,
            category=category,
            quantity =quantity,
            vendor=vendor,
            price=price,
            date=date,)
    
    u.save()
    return render(req, 'app1/form2.html',{'name':name})

@login_required
def save_print(req):
    for temp in Temp.objects.all():
        u = Req(
            faculty = temp.faculty,
            code = temp.code,
            category = temp.category,
            item = temp.item,
            quantity = temp.quantity,
            price = temp.price,
            vendor = temp.vendor,
            date = datetime.now(),
        )
        u.save()
       
    Temp.objects.all().delete()
    return redirect('/home/')



def logout_view(req):
    logout(req)
    return redirect('/')

@login_required
def update(req):
    id=req.GET['id']
    stock = req.GET['stock']
    category =req.GET['category']
    doi = req.GET['Last_DOI']
    record = Inventory.objects.get(id=id)
    item = record.item
    u = Inventory(
            id = id,
            item = item,
            stock = stock,
            doi = doi,
            category = category,
        )
    u.save()
    return render(req, 'app1/alert.html',{'mess':'Data Updated Successfully'})


@login_required
def add_item(req): 
    item=req.GET['item']
    item=item.upper()
    category =req.GET['category']
    stock = req.GET['stock']
    doi = req.GET['Last_DOI']
    
    u = Inventory(
        item = item,
        stock = stock,
        doi = doi,
        category = category,
            )
    u.save()
    return render(req, 'app1/alert.html',{'mess':'Item Added Successfully'})