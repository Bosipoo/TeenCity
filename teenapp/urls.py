from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addteen/',views.addTeen.as_view(), name="addteen"),
    path('teens/',views.teenLanding.as_view(), name="teenlanding"),
    path('teens/view/<int:pk>/',views.view_teen_in_detail.as_view(), name="viewteen"),
    path('teens/edit/<int:pk>/',views.edit_teen_details.as_view(), name="editteen"), 
    path('teens/delete/<int:pk>/',views.delete_teen.as_view(), name="deleteteen"),
]
 