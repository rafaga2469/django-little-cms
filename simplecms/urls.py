from django.urls import path
from simplecms import views as simplecms_views

urlpatterns = [
    path('', simplecms_views.BaseCmsView.as_view(), name='base_cms'),
    path('site/<str:menu_option_slug>',
         simplecms_views.BaseCmsView.as_view(),
         name='base_cms'),
    path('site/<str:menu_option_slug>/<str:article_slug>',
         simplecms_views.ArticleDetailView.as_view(),
         name='article_detail'),
]
