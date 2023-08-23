from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.registerPage),
    path('login/',views.loginPage),
    path('logout/',views.logoutView),
    path('barang/', include("API.barang.urls"))
]
