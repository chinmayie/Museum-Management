from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views
#from django.urls import url,include
from . import views
urlpatterns=[
     url(r'^home$',views.home,name='home'),
     url(r'^bookonline$',views.bookonline,name='bookonline'),
     url(r'^ticket$',views.ticket,name='ticket'),
     url(r'^payment$',views.payment,name='payment'),
     url(r'^finalpayment$',views.finalpayment,name='finalpayment'),
     url(r'^gallery$',views.gallery,name='gallery'),
     url(r'^timings$',views.timings,name='timings'),
     url(r'^divisions$',views.divisions,name='Divisions'),
     url(r'^items$',views.items,name='Items'),
     url(r'^staff',views.staff,name='Staff'),
     url(r'^admin_page$',views.admin_page,name='admin_page'),
     url(r'^exhibition$',views.exhibition,name='Exhibition'),
     url(r'^book$',views.book,name='book'),
     url(r'^after_book$',views.after_book,name='after_book'),
     url(r'^contact$',views.contact,name='contact'),
     url(r'^display$',views.display,name='display'),
     url(r'^about$',views.about,name='about'),
     url(r'^exh_search/$', views.exh_search, name='exh_search'),
     url(r'^dept_search/$', views.dept_search, name='dept_search'),
     url(r'^vis_search/$',views.vis_search, name='vis_search'),
     url(r'^emp_search/$',views.emp_search, name='emp_search'),
     url(r'^delete/$',views.delete_staff,name='delete_staff'),
     url(r'^item_search/$',views.item_search,name='item_search'),
     url(r'^delete_division/$',views.delete_division,name='delete_division'),
     url(r'^delete_item/$',views.delete_item,name='delete_item'),
     url(r'^delete_exhibition/$',views.delete_exhibition,name='delete_exhibition'),
     url(r'^delete_visitors/$',views.delete_visitors,name='delete_visitors'),
     url(r'^display_date/$',views.display_date,name='display_date'),
     url(r'^query1/$',views.query1,name='query1'),
     url(r'^query2/$',views.query2,name='query2'),
     #url(r'^logout/$',views.logout, name='logout'),
]
