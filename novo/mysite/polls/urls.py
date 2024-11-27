from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/só para achar
    path('', views.index, name='index'),
    # ex: /polls/5/questionario né
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/resultados/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/votação/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
