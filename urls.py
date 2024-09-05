"""
URL configuration for waste_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.customer_registration,name = 'Login_page'),
    path('customers', include('customers.urls')), 
    path('',views.custom_login_view , name='login_page') , 
    path('homepage/',views.homepage,name= "Home"),
    path('report_page/',views.sanitation_report,name="Report_Page"),
    path('fact/',views.facts , name="Facts"),
    path('Recycle_guide/',views.Recycling_guide,name="Recycle_Guide"),
    path('DashBoard/',views.waste_dashBoard,name="Analysis_DashBoard"),
    path('Waste_Schedule/',views.Waste_Schedule,name="Waste_Schedule_page"),
    path('Waste_FAQ/',views.Waste_FAQ,name="Waste_FAQ_Page"),
    path('Waste_Quiz/',views.Waste_Quiz,name="Waste_Quiz"),
    # path('user_list/',views.user_list,name='user_list'),
    path('chat/',views.chat_view , name='chat_view'),
    path('generater_page/',views.generater_page , name='generater_page')
]
