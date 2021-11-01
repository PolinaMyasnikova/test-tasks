from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('cat/<slug:cat_slug>/', show_cat, name='post'),
    path('category/<int:vil_id>', show_category, name='village')
]
