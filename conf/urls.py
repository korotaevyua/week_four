"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

import vacancies.views as vacancies_views
from vacancies.views import custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', vacancies_views.main_view, name='main'),
    path('vacancies/', vacancies_views.vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:category>/', vacancies_views.cat_view, name='category'),
    path('companies/<int:company_id>/', vacancies_views.companies_view, name='company'),
    path('vacancies/<int:vacancy_id>/', vacancies_views.one_vac_view, name='vacancy'),
    path('admin/', admin.site.urls),
]
