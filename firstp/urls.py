"""
URL configuration for firstp project.

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
from django.urls import path
from firstp import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('',views.HomePage),
    path('login/',views.Login),
    path('signup/',views.Signup),
    path('savedetails/',views.saveDetails,name="savedetails"),
    path('about-us/', views.aboutUs),
    path('contact-us/', views.contactUs),
    path('course/', views.course),
    path('course/<courseid>', views.courseDetails),
    path('form/',views.Form),
    path('submitform/', views.submitform, name="submitform"),
    path('calculator/',views.calculator),
    path('evenodd/',views.EvenOdd,name="evenodd"),
    path('marksheet/',views.Marksheet)
 ]
