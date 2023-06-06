from django.urls import path
from . import views


urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('comments/<int:pk>/', views.AddComment.as_view(), name='AddComments'),
               path('<int:pk>/add_like/', views.Addlikes.as_view(), name='AddLikes'),
               path('<int:pk>/del_like/', views.Dislike.as_view(), name='Dellikes')]