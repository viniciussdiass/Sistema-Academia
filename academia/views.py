from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import PlanoTreino, Aluno
from django import forms



class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'email', 'telefone', 'plano']
        widgets = {
            'plano': forms.Select(attrs={'class': 'form-control'})
        }



class PlanoTreinoListView(ListView):
    model = PlanoTreino
    template_name = 'academia/plano_list.html'


class PlanoTreinoDetailView(DetailView):
    model = PlanoTreino
    template_name = 'academia/plano_detail.html'


class PlanoTreinoCreateView(CreateView):
    model = PlanoTreino
    fields = ['nome', 'descricao', 'valor_mensal']
    template_name = 'academia/plano_form.html'
    success_url = reverse_lazy('plano_list')


class PlanoTreinoUpdateView(UpdateView):
    model = PlanoTreino
    fields = ['nome', 'descricao', 'valor_mensal']
    template_name = 'academia/plano_form.html'
    success_url = reverse_lazy('plano_list')


class PlanoTreinoDeleteView(DeleteView):
    model = PlanoTreino
    template_name = 'academia/plano_confirm_delete.html'
    success_url = reverse_lazy('plano_list')



class AlunoListView(ListView):
    model = Aluno
    template_name = 'academia/aluno_list.html'


class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'academia/aluno_detail.html'


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'academia/aluno_form.html'
    success_url = reverse_lazy('aluno_list')


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'academia/aluno_form.html'
    success_url = reverse_lazy('aluno_list')


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'academia/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')
