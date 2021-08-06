from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('courses/create',views.create),
    path('courses/predestroy/<int:id>',views.predestroy),
    path('courses/destroy/<int:id>',views.destroy),
    # path('courses/<int:id>',views.course),
    # path('courses/edit/<int:id>',views.edit),
    # path('courses/update/<int:id>',views.update),
    # 
]
