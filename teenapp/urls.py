from django.urls import include,path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from . import views

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    # path('accounts/login/', views.login_view, name="login"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('teens/addteen/',views.addTeen.as_view(), name="addteen"),
    path('teens/',views.teenLanding.as_view(), name="teenlanding"),
    path('teens/view/<int:pk>/',views.view_teen_in_detail.as_view(), name="viewteen"),
    path('teens/edit/<int:pk>/',views.edit_teen_details.as_view(), name="editteen"), 
    path('teens/delete/<int:pk>/',views.delete_teen.as_view(), name="deleteteen"),
    path('search-with-date/',views.search_date, name="datesearch"),
    path('profile/<str:username>/', views.UserDetailView.as_view(), name="userprofile"),
]
  