"""NodeViz_Project URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "get-binary-tree-impl/", views.get_binary_tree_impl, name="get_binary_tree_impl"
    ),
    path(
        "get-linked-list-impl/", views.get_linked_list_impl, name="get_linked_list_impl"
    ),
    path("get-recursion-impl/", views.get_recursion_impl, name="get_recursion_impl"),
]
