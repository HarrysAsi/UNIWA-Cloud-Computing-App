from django.urls import path
from .views import (
    index_view,
    login_view,
    logout_view,
    main_view,
)

urlpatterns = [
    path('', index_view, name='main'),
    path('main/', main_view, name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
