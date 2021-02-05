from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#template tagging
app_name = 'APS_app'

urlpatterns = [
    url(r'^login.html/$',views.user_login,name='user_login'),
    url(r'^registration.html/$',views.register,name='register'),
    url(r'^contact.html/$',views.contact,name='contact'),
    url(r'^services.html/$',views.services,name='services'),
    url(r'^upcoming.html/$',views.upcoming,name='upcoming'),
    url(r'^about.html/$',views.about,name='about'),
    url(r'^food.html/$',views.food,name='food'),
    url(r'^clothes.html/$',views.clothes,name='clothes'),
    url(r'^blood.html/$',views.blood,name='blood'),
    url(r'^index.html/$',views.index,name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
