from django.urls import path
from myapp import views


urlpatterns = [
    path('myfunction/',views.myfunction,name="myfunction"),
    path('function2/',views.function2,name="function2"),
    path('firsthtmlpage/',views.firsthtmlpage,name="firsthtmlpage"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('savedata/',views.savedata, name="savedata"),
    path('imgpage/',views.imgpage, name="imgpage"),
    path('imagesave/', views.imagesave, name="imagesave"),
    path('img/',views.img,name="img")
]
