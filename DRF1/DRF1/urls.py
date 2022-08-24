
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.student_details),
    path('stuList/<int:pk>',views.student_details_byId),
    path('stuList/',views.student_list)
]
