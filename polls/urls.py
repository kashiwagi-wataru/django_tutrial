from django.urls import path

from . import views

# from rest_framework import routers

# from .views import QuestionViewSet, ChoiceViewSet

# router = routers.DefaultRouter()
# router.register(r'Question', QuestionViewSet)
# router.register(r'Choice', ChoiceViewSet)


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultView.as_view(),name="results"),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]



