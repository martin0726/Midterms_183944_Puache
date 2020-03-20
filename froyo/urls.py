from django.conf.urls import url

from .views import IngredientsListView, IngredientsDetailView, IngredientsUpdateView, IngredientsCreateView, RecipesListView, RecipesDetailView, RecipesUpdateView, RecipesCreateView, OrdersListView, OrdersDetailView, OrdersUpdateView, OrdersCreateView
 
urlpatterns = [
		url(r'^ingredients_list$', IngredientsListView.as_view(), name='Ingredients_List_show'),
		url(r'^ingredients_detail$', IngredientsDetailView.as_view(), name='Ingredients_Detail_show'),
		url(r'^ingredients_update$', IngredientsUpdateView.as_view(), name='Ingredients_Update_show'),
		url(r'^ingredients_create$', IngredientsCreateView.as_view(), name='Ingredients_Create_show'),

]	