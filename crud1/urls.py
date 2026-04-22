from . import views
from django.urls import path


urlpatterns = [
    
    path("get_user/", views.get_user),
    path("post_user/", views.post_user),
    path("user/", views.user),
    path("api-final-test/", views.api_final_test, name="api_final_test"),
]