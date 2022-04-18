from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/', views.aboutMe),
    path('', views.landing),
    path('memo_form/', views.memo),
    path('memo_form/new_memo/', views.new_memo),
    path('memo_form/#<int:pk>/', views.MemoUpdate.as_view()),
   # path('update_memo/<int:pk>/', views.update_memo),
    path('delete_memo/<int:pk>/', views.delete_memo),
    # path('memo/', views.MemoDetail.as_view()),
]