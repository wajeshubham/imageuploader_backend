from django.urls import path

from .views import upload_img, ImageView, delete_img

urlpatterns = [
    path('upload/', upload_img, name='upload'),
    path('images/', ImageView.as_view(), name='images'),
    path('image/<int:img_id>/delete/', delete_img, name='delete_img'),
]
