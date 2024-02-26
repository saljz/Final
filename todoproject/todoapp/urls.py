from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [

    path('', views.add, name='add'),
    # path('details',views.detail ,name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('list-home/', views.TasklistView.as_view(), name='list-home'),
    path('detail-home/<int:pk>/', views.TaskDetailView.as_view(), name='detail-home'),

]
