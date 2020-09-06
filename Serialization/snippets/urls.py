from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

#제공된 각 URL 패턴에 추가 된 형식 접미사 패턴을 포함하는 URL 패턴 list를 반환
urlpatterns = format_suffix_patterns(urlpatterns)