from django.shortcuts import render
from django.views import generic


class IngredientsListView(generic.ListView):
	template_name = 'ingredients_list.html'


class IngredientsDetailView(generic.DetailView):
	template_name = 'ingredients_detail.html'


class IngredientsUpdateView(generic.UpdateView):
	template_name = 'ingredients_update_form.html'


class IngredientsCreateView(generic.CreateView):
	template_name = 'ingredients_create_form.html'


class RecipesListView(generic.ListView):
	template_name = 'recipes_list.html'


class RecipesDetailView(generic.DetailView):
	template_name = 'recipes_detail.html'


class RecipesUpdateView(generic.UpdateView):
	template_name = 'recipes_update_form.html'


class RecipesCreateView(generic.CreateView):
	template_name = 'recipes_create_form.html'
# Create your views here.
