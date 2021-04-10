from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=32)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return self.code


class Specialty(models.Model):
    code = models.CharField(max_length=128, primary_key=True, unique=True)
    title = models.CharField(max_length=128)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.code
