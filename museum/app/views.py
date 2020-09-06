# -*- coding: utf-8 -*-

# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
from .forms import Visitor,Division,Item,employee,Exhibitions
import json
from .models import Visitors,Exhibition,Divisions,Staff,Items
from .filters import UserFilter,UserFilter1,UserFilter2,UserFilter3,UserFilter4
from django.db import connection
from django.db.models import Sum
from django.core.serializers.json import DjangoJSONEncoder
import datetime
def dept_search(request):
    #return render(request, 'proj/home_page.html')
    user_list = Divisions.objects.all()
    user_filter = UserFilter4(request.GET, queryset=user_list)
    return render(request, 'app/dept_search.html', {'filter': user_filter})
def item_search(request):
    user_list = Items.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'app/item_search.html', {'filter': user_filter})
def exh_search(request):
    #return render(request, 'proj/home_page.html')
    user_list = Exhibition.objects.all()
    user_filter = UserFilter1(request.GET, queryset=user_list)
    return render(request, 'app/user_list.html', {'filter': user_filter})
def vis_search(request):
    #return render(request, 'proj/home_page.html')
    user_list = Visitors.objects.all()
    user_filter = UserFilter2(request.GET, queryset=user_list)
    return render(request, 'app/vis_list.html', {'filter': user_filter})
def emp_search(request):
    #return render(request, 'proj/home_page.html')
    user_list = Staff.objects.all()
    user_filter = UserFilter3(request.GET, queryset=user_list)
    return render(request, 'app/emp_search.html', {'filter': user_filter})
def home(request):
    return render(request, 'app/home_page.html')
def timings(request):
    return render(request, 'app/timings.html')
def divisions(request):
    form= Division(request.POST)
    if form.is_valid():
     obj=form.save()
    context={'form': form}
    return render(request, 'app/dep_reg.html', context)
def items(request):
    form= Item(request.POST)
    if form.is_valid():
        obj=form.save()
    context={'form': form}
    return render(request, 'app/item_reg.html', context)
def staff(request):
    form= employee(request.POST)
    if form.is_valid():
        obj=form.save()
    context={'form': form}
    return render(request, 'app/emp_reg.html', context)
def exhibition(request):
    form= Exhibitions(request.POST)
    if form.is_valid():
        obj=form.save()
    context= {'form': form }
    return render(request, 'app/exh_reg.html', context)
def display(request):
    return render(request, 'app/exhibition_list.html')
def contact(request):
    return render(request, 'app/contact.html')
def about(request):
    return render(request,'app/about.html')
def admin_page(request):
    return render(request,'app/admin.html')
def gallery(request):
    return render(request,'app/Gallery.html')
def book(request):
    form= Visitor()
    return render(request, 'app/book1.html',{})
def after_book(request):
    if request.method=='POST':
       form=Visitor(request.POST or None)
       if form.is_valid():
          obj=form.save(commit=False)
          cost=(obj.adult_ticket*50)+(obj.child_ticket*30)
          obj.cost=cost
          obj.save()
    return render(request, 'app/cost.html',{'adultticket':obj.adult_ticket,'childticket':obj.child_ticket,'cost':obj.cost})
def bookonline(request):
    form= Visitor(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        context= {'form':form }
        return render(request, 'app/book2.html', context)
def ticket(request):
    form=Visitor()
    if request.method=='POST':
        form=Visitor(request.POST)
        if form.is_valid():
           date=form.cleaned_data['visitdate']
           sdate=date.__str__()
           obj=form.save(commit=False)
           cost=(obj.adult_ticket*50)+(obj.child_ticket*30)
           obj.cost=cost
           request.session.__setitem__('vdate',sdate)
           request.session.__setitem__('adult_ticket',obj.adult_ticket)
           request.session.__setitem__('child_ticket',obj.child_ticket)
           request.session.__setitem__('cost',cost)
    return render(request, 'app/ticket.html',{'adult_ticket':obj.adult_ticket,'child_ticket':obj.child_ticket,'cost':obj.cost,'visitdate':obj.visitdate})
def payment(request):
    return render(request,'app/payment.html',{'cost':request.session['cost']})
def finalpayment(request):
    final=Visitors.objects.create(adult_ticket=request.session['adult_ticket'],child_ticket=request.session['child_ticket'],cost=request.session['cost'],visitdate=request.session['vdate'])
    return render(request,'app/finalpayment.html',{'vdate':request.session['vdate'],'adticket':request.session['adult_ticket'],'chticket':request.session['child_ticket'],'cost':request.session['cost']});
def login(request):
    return render(request,'app/login.html')
def demo(request) :
    return render(request, 'app/demo.html')
def delete_staff(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        p = Staff.objects.get(sid=sid)
        p.delete()
    return render(request, 'app/delete.html', {})
def delete_division(request):
    if request.method=='POST':
        divid=request.POST.get('divid')
        p = Divisions.objects.get(divid=divid)
        p.delete()
    return render(request, 'app/delete_divisions.html', {})
def delete_item(request):
    if request.method=='POST':
        itemid=request.POST.get('itemid')
        p = Items.objects.get(itemid=itemid)
        p.delete()
    return render(request, 'app/delete_item.html', {})
def delete_exhibition(request):
    if request.method=='POST':
        eid=request.POST.get('eid')
        p = Exhibition.objects.get(eid=eid)
        p.delete()
    return render(request, 'app/delete_exhibition.html', {})
def display_date(request):
    if request.method=='POST':
       p = Visitors.objects.get(visitdate)
    return render(request,'app/display_visitors.html',{cost})
          
def delete_visitors(request):
    if request.method=='POST':
        tran_no=request.POST.get('tran_no')
        p = Visitors.objects.get(tran_no=tran_no)
        p.delete()
    return render(request, 'app/delete_visitors.html', {})
                                    
def query1(request):
    cost=Visitors.objects.all().aggregate(total=Sum('cost'))
    return render(request,'app/submit.html',{'cost':cost,})
def query2(request):
    cursor=connection.cursor()
    cursor.execute("select i.itemid,d.divid,d.floorno,d.hallno,i.description from app_divisions d,app_items i where d.divid=i.divid_id ") 
    row=cursor.fetchall()
    print(row)
    return render(request,'app/query2.html',{'row':row,})
