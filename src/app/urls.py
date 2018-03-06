from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:post_id>', views.add_comment, name="add_comment"),
	path('comment/<int:comment_id>', views.update_comment, name="update_comment"),
	path('comment/<int:comment_id>/delete', views.delete_comment, name="delete_comment")
]