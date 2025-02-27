"""adminCustomization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blog.admin import blog_site
from bookstore.admin import bookstore_site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/',blog_site.urls),
    path('bookstoreadmin/',bookstore_site.urls),
]

'''Change the site index title'''
#admin.site.index_title = "Customized Title"
#admin.site.site_header = "The BookStore Admin"
#admin.site.site_title="Bookstore"