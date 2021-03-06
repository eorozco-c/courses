from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('courses/create',views.create),
    path('courses/predestroy/<int:id>',views.modal_view),
    path('courses/destroy/<int:id>',views.destroy),
    path('courses/comment/<int:id>',views.comment),
    path('courses/comment/create/<int:idCurso>',views.create_comment),
]
