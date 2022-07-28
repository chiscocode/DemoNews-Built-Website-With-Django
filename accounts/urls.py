from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [

    path('contact/', views.ContactUs,name="contact"),
    path('about/', views.AboutUs,name="about"),




    path('', views.home,name="home"),
    path('<slug:category_slug>/', views.category,name="category"),
    path('postdetail/<str:slug>/', views.MainPostdetail,name="mainpostdetails"),
    path('detail/<str:slug>/', views.PostDetail,name="postdetails"),
    path('featureddetail/<str:slug>/', views.FeaturedDetail,name="featureddetails"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)