import os

import django

import data
from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

if __name__ == '__main__':
    for speciality in data.specialties:
        Specialty.objects.create(code=speciality['code'], title=speciality['title'])

    for company in data.companies:
        Company.objects.create(name=company['title'], location=company['location'], description=company['description'],
                               employee_count=company['employee_count'])
    for job in data.jobs:
        spec = Specialty.objects.get(code=job['specialty'])
        spec.save()
        comp = Company.objects.get(id=job['company'])
        comp.save()
        Vacancy.objects.create(title=job['title'], specialty=spec, company=comp,
                               skills=job['skills'], description=job['description'], salary_min=job['salary_from'],
                               salary_max=job['salary_to'], published_at=job['posted'])
