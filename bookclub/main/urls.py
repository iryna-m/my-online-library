from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    # path('sign-up/', views.sign_up, name='sign-up'),
    # path('book/<int:bookid/>', views.book, name='book')
]