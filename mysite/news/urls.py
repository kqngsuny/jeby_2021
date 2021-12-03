from django.urls import path
from .views import base_views, keyword_views, site_views

app_name = "news"

urlpatterns = [
    path("", base_views.index, name="index"),
    path("search/", base_views.news_search, name="news_search"),
    path("keyword/", keyword_views.KeywordList.as_view(), name="keyword_list"),
    path(
        "keyword/create/", keyword_views.KeywordCreate.as_view(), name="keyword_create"
    ),
    path(
        "keyword/update/<int:pk>/",
        keyword_views.KeywordUpdate.as_view(),
        name="keyword_update",
    ),
    path(
        "keyword/delete/<int:pk>/",
        keyword_views.KeywordDelete.as_view(),
        name="keyword_delete",
    ),
    path("site/create/", site_views.SiteCreate.as_view(), name="site_create"),
    path("site/update/<int:pk>/", site_views.SiteUpdate.as_view(), name="site_update"),
]