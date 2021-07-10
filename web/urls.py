from django.urls import path
from .import views
from .views import home, librodiario,balance, TestBalance

#app_name='web'
urlpatterns = [
    path('', home, name="home"),
    path('librodiario/', librodiario, name="librodiario"),
    path('balance/', balance, name="balance"),
    path('TestBalance/', TestBalance, name="TestBalance"),

]