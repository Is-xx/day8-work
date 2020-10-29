from django.urls import path
from test_app import views

urlpatterns = [
    path('teacher/', views.TeacherAPIView.as_view()),
    path('teacher/<str:id>', views.TeacherAPIView.as_view()),
]
