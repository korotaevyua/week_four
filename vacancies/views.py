from django.db.models import Count
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render

from vacancies.models import Vacancy, Company, Specialty


def main_view(request):
    context = {'all_spec': Specialty.objects.annotate(Count('vacancies')),
               'all_comp': Company.objects.annotate(Count('vacancies'))}
    return render(request, "vacancies/index.html", context=context)


def vacancies_view(request):
    context = {'all_jobs': Vacancy.objects.select_related("specialty")}
    return render(request, "vacancies/vacancies.html", context=context)


def cat_view(request, category):
    context = {'all_jobs_of_cat': Vacancy.objects.filter(specialty__code=category),
               'category_title': Specialty.objects.filter(code=category)[0].title}
    return render(request, "vacancies/category.html", context=context)


def companies_view(request, company_id):
    context = {'company': Company.objects.filter(id=company_id).annotate(Count('vacancies'))[0],
               'vacancy_of_company': Vacancy.objects.filter(company__id=company_id).select_related("specialty")}
    return render(request, "vacancies/company.html", context=context)


def one_vac_view(request, vacancy_id):
    that_vacancy = Vacancy.objects.filter(id=vacancy_id)
    context = {'vacancy': that_vacancy.select_related("specialty").select_related("company")[0]}
    return render(request, "vacancies/vacancy.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
