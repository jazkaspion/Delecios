from django.urls import path
from .views import *
from .recipes import views as rec_views
from .categorie import views as cat_views


urlpatterns = [
    path('', index, name="dashboard-home"),
    path('rec/list/', rec_views.rec_list, name='rec_list'),
    path('rec/detail/<int:pk>/', rec_views.rec_detail, name='rec_detail'),
    path('rec/add/', rec_views.rec_add, name='rec_add'),
    path('rec/edit/<int:pk>', rec_views.edit, name='rec_edit'),
    path('rec/del/<int:pk>', rec_views.rec_delete, name='rec_del'),

    path('cat/list/', cat_views.list, name='cat_list'),
    path('cat/del/<int:pk>/', cat_views.delete, name='cat_del'),
    path('cat/edit/<int:pk>/', cat_views.cat_edit, name='cat_edit'),
    path('cat/one/<int:pk>/', cat_views.one, name='cat_one'),
    path('cat/add/', cat_views.cat_add, name='cat_add'),

]















