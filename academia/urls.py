from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='home'),  
    path('planos/', views.PlanoTreinoListView.as_view(), name='plano_list'),
    path('planos/create/', views.PlanoTreinoCreateView.as_view(), name='plano_create'),
    path('planos/<int:pk>/', views.PlanoTreinoDetailView.as_view(), name='plano_detail'),
    path('planos/<int:pk>/update/', views.PlanoTreinoUpdateView.as_view(), name='plano_update'),
    path('planos/<int:pk>/delete/', views.PlanoTreinoDeleteView.as_view(), name='plano_delete'),
    
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('alunos/create/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('alunos/<int:pk>/update/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    path('alunos/<int:pk>/delete/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
]
