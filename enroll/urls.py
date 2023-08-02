from django.urls import path
from enroll import views
urlpatterns = [
    path("", views.add_show , name="addandshow"),
    path("delete_data/<int:id>", views.delete_data , name="delete"),
    path("update_data/<int:id>", views.update_data , name="update"),

]