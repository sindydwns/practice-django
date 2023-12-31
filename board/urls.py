from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/answer', views.answer_create, name='answer_create')
]
