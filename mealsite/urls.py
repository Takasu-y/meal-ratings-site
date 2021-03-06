from django.urls import path
from .views import IndexView, MealListView, MealDetailView

app_name='meal'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('List/<str:category>/', MealListView.as_view(), name="mealList"),
    path('detail/<int:pk>/', MealDetailView.as_view(), name="mealDetail"),

]
