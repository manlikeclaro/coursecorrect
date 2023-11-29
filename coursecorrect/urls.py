"""
URL configuration for coursecorrect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coursecorrect import settings
from mainapp import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('search', views.product_search, name='search'),
                  path('category', views.product_category, name='category'),
                  path('shop', views.shop, name='shop'),
                  path('product/<int:id>', views.product, name='product'),
                  path('product/update/<int:product_id>', views.product_update, name='product-update'),
                  path('product/delete/<int:product_id>', views.product_delete, name='product-delete'),
                  path('confirmation', views.confirmation, name='confirmation'),
                  path('profile', views.profile, name='profile'),
                  path('update-profile', views.update_profile, name='update-profile'),
                  path('update-profile-details', views.update_profile_details, name='update-profile-details'),
                  path('address', views.address, name='address'),
                  path('about', views.about, name='about'),
                  path('sign-in', views.sign_in, name='sign-in'),
                  path('sign-up', views.sign_up, name='sign-up'),
                  path('logout', views.sign_out, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
