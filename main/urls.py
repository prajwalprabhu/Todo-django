from django.urls import path
from . import views
urlpatterns = [
    path('init/', views.init),
    path('new/<str:name>/<str:date>', views.new),
    path('rm/<int:i>', views.rm)
]
