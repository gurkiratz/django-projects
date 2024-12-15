from django.contrib import admin
from django.db import models


# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CompletedCourse(Course):
    grade_achieved = models.CharField(max_length=2)


class OngoingCourse(Course):
    remaining_seats = models.IntegerField()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    courses_enrolled_in = models.ManyToManyField(
        OngoingCourse, related_name="enrolled_students", blank=True
    )
    courses_completed = models.ManyToManyField(
        CompletedCourse, related_name="completed_students", blank=True
    )

    def __str__(self):
        return self.name


# Register models in admin
admin.site.register(Course)
admin.site.register(CompletedCourse)
admin.site.register(OngoingCourse)
admin.site.register(Student)
