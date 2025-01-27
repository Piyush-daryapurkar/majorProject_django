from django.urls import path

from . import views

urlpatterns = [
    path("",views.animesh),
    path("/super",views.Super_dashboard,name="super"),
    path("/manager",views.Manager_login,name="manager")

]

