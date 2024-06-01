from django.urls import path
#from news.api.views import article_list_create_api_view, article_detail_api_view
from news.api.views import ArticleListCreateAPIView, ArticalDetailAPIView, JournalistCreateAPIView

urlpatterns = [
    # path("articles/", article_list_create_api_view, name="articles-list"),
    # path("articles/<int:pk>/", article_list_create_api_view, name="article-detail")

    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticalDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistCreateAPIView.as_view(), name="journalist-list")

]