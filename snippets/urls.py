from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('accounts/', views.UserList.as_view(), name='account-list'),
    path('accounts/<int:pk>/', views.UserDetail.as_view(), name='account-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
