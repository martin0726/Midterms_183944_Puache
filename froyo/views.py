from django.shortcuts import render
from django.views import generic


class IngredientsListView(generic.ListView):
	template_name = 'ingredients_list.html'


class IngredientsDetailView(generic.DetailView):
	template_name = 'ingredients_detail.html'


class IngredientsUpdateView(generic.Updateview):
	template_name = 'ingredients_update_form.html'


class IngredientsCreateView(generic.CrateView):
	template_name = 'ingredients_create_form.html'


# Create your views here.
