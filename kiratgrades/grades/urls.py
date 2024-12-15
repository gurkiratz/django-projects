from django.urls import path

from grades.views import (
    api_overview,
    get_all_ongoing_courses,
    get_all_students,
    get_grade_of_completed_course,
    get_student_average_grade,
    get_student_completed_courses,
    get_student_details,
    get_student_ongoing_courses,
)

urlpatterns = [
    path("", api_overview, name="api_overview"),
    path("students/", get_all_students, name="get_all_students"),
    path("ongoing-courses/", get_all_ongoing_courses, name="get_all_ongoing_courses"),
    path("student-details/", get_student_details, name="get_student_details"),
    path(
        "student-average-grade/",
        get_student_average_grade,
        name="get_student_average_grade",
    ),
    path(
        "student-ongoing-courses/",
        get_student_ongoing_courses,
        name="get_student_ongoing_courses",
    ),
    path(
        "student-completed-courses/",
        get_student_completed_courses,
        name="get_student_completed_courses",
    ),
    path(
        "completed-course-grade/",
        get_grade_of_completed_course,
        name="get_grade_of_completed_course",
    ),
]
