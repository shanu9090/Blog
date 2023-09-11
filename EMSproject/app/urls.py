#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),

    #********************************************************************

    path('adminreg/', views.adminreg,name="adminreg"),
    path('admininsert/',views.adminreginsert,name="adminreginsert"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlgin/',views.adminlogininsert,name="adminlogininsert"),
    path('displayrecord/',views.displayrecord,name="displayrecord"),

    #***********************************************************************

    path('userreg/', views.userreg,name="userreg"),
    path('userregister',views.userreginsert,name="userreginsert"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogininsert/',views.userlogininsert,name="userlogininsert"), 
    path('insertrecord/',views.insertrecord,name="insertrecord"),
    path('quiryinsert/',views.quiryinsert,name="quiryinsert"),

    #&*****************************************************************

    path('updatepage/<int:pk>',views.updatepage,name="updatepage"),
    path('update/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="deletepage")



]
