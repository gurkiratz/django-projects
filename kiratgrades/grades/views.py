from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CompletedCourse, OngoingCourse, Student
from .serializers import (
    CompletedCourseSerializer,
    OngoingCourseSerializer,
    StudentSerializer,
)


@api_view(["GET"])
def api_overview(request):
    """
    Return a list of all API routes.
    """
    api_urls = {
        "Get All Students": reverse("get_all_students"),
        "Get All Ongoing Courses": reverse("get_all_ongoing_courses"),
        "Get Student Details": reverse("get_student_details"),
        "Get Student Average Grade": reverse("get_student_average_grade"),
        "Get Student Ongoing Courses": reverse("get_student_ongoing_courses"),
        "Get Student Completed Courses": reverse("get_student_completed_courses"),
        "Get Grade of Completed Course": reverse("get_grade_of_completed_course"),
    }
    return Response(api_urls)


# Create your views here.
@api_view(["GET"])
def get_all_students(request):
    """
    Retrieve all students.
    """
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def get_student_details(request):
    """
    Retrieve details of a student by student ID.
    """
    student_id = request.data.get("student_id")
    try:
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
def get_student_average_grade(request):
    """
    Retrieve the average grade of a student by student ID.
    """
    student_id = request.data.get("student_id")
    try:
        student = Student.objects.get(id=student_id)
        completed_courses = student.courses_completed.all()
        if not completed_courses:
            return Response({"average_grade": "N/A"})
        total_grade = 0
        for course in completed_courses:
            total_grade += int(course.grade_achieved)
        average_grade = total_grade / len(completed_courses)
        return Response({"average_grade": average_grade})
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def get_all_ongoing_courses(request):
    """
    Retrieve all ongoing courses.
    """
    ongoing_courses = OngoingCourse.objects.all()
    serializer = OngoingCourseSerializer(ongoing_courses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def get_student_ongoing_courses(request):
    """
    Retrieve ongoing courses of a student by student ID.
    """
    student_id = request.data.get("student_id")
    try:
        student = Student.objects.get(id=student_id)
        ongoing_courses = student.courses_enrolled_in.all()
        serializer = OngoingCourseSerializer(ongoing_courses, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
def get_student_completed_courses(request):
    """
    Retrieve completed courses of a student by student ID.
    """
    student_id = request.data.get("student_id")
    try:
        student = Student.objects.get(id=student_id)
        completed_courses = student.courses_completed.all()
        serializer = CompletedCourseSerializer(completed_courses, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
def get_grade_of_completed_course(request):
    """
    Retrieve the grade of a completed course by student ID and course name.
    """
    student_id = request.data.get("student_id")
    course_name = request.data.get("course_name")
    try:
        student = Student.objects.get(id=student_id)
        completed_course = student.courses_completed.get(name=course_name)
        return Response({"grade_achieved": completed_course.grade_achieved})
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except CompletedCourse.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
