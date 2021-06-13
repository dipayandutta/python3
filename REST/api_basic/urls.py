from django.urls import path 
from .views import (article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,
		GenericAPIListall)


urlpatterns = [
	path('article/',article_list),
	path('articleclass/',ArticleAPIView.as_view()),
	path('articledetails/<int:id>/',ArticleDetails.as_view()),
	path('detail/<int:pk>/',article_detail),
	path('genericlist/<int:id>/',GenericAPIView.as_view()),
	path('genericlistall/',GenericAPIListall.as_view())
		
]

