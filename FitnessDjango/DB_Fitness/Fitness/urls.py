from django.urls import path
from Fitness import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path("",views.login, name='login'),
    path("signup/",views.signup,),
    path("main/",views.main,name='main'),
    path("main/proteintake",views.proteintake,),
    path("main/maintance",views.maintance,),
    path("main/bmi",views.bmi,),
    path("signup/addData",views.addData,name="addData"),
    path('api/get-data/', views.getdata, name='get_data'),
]



urlpatterns += staticfiles_urlpatterns()