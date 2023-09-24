from django.contrib import admin
from django.urls import path, include
from pizza import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('admin1', views.admin1, name='admin1'),
    path('submit-task/', views.submit_work, name='home'),
    path("success/",views.Success,name="Success"),
    path('accounts', views.superadmin, name = 'superadmin'),
    path('login/', views.login_page, name = 'login'),
    path('authorized', views.authorized, name='authorized'),
    path('dummy', views.dummy, name='dummy'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
