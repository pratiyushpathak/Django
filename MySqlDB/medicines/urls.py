from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='med'),
    # path('show/', views.show, name='show'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.destroy, name='delete'),
]