from rest_framework import serializers

from .models import CompletedCourse, Course, OngoingCourse, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "department", "description"]


class CompletedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedCourse
        fields = ["id", "name", "department", "description", "grade_achieved"]


class OngoingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OngoingCourse
        fields = ["id", "name", "department", "description", "remaining_seats"]


class StudentSerializer(serializers.ModelSerializer):
    courses_enrolled_in = OngoingCourseSerializer(many=True)
    courses_completed = CompletedCourseSerializer(many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "department",
            "semester",
            "courses_enrolled_in",
            "courses_completed",
        ]
