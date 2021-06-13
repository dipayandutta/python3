from django.urls import path 
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails

urlpatterns = [
	path('article/',article_list),
	path('articleclass/',ArticleAPIView.as_view()),
	path('articledetails/<int:id>/',ArticleDetails.as_view()),
	path('detail/<int:pk>/',article_detail)
		
]

