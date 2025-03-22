from django.urls import path
from blog.views import category, post, comment, like_dislike, bookmark

app_name = 'blog'


urlpatterns = [
    path('categories/', category.category_list, name='category-list'),
    path('category/<int:pk>', category.category_detail, name='category-detail'),

    path('pots/', post.post_list, name='post-list'),
    path('post/<int:pk>',post.post_detail, name='post-detail'),
    path('post/create/',post.post_create, name='post-create'),
    path('post/<int:pk>/edit/',post.post_edit, name='post-edit'),
    path('post/<int:pk>/delete/',post.post_deletes, name='post-delete'),
    path('posts/<int:pk>/comment/', comment.add_comment, name='comment-add'),
    path('comments/<int:pk>/delete/', comment.delete_comment, name='comment-delete'),
    path('posts/<int:pk>/like/', like_dislike.toggle_like, name='toggle-like'),
    path('posts/<int:pk>/dislike', like_dislike.toggle_dislike, name='toggle-dislike'),
    path('bookmarks/', bookmark.bookmarks_list, name='bookmark-list'),
    path('bookmarks/<int:pk>/delete/', bookmark.bookmark_delete, name='bookmark-delete'),
    path('posts/<int:pk>/bookmark/', bookmark.toggle_bookmark, name='toggle-bookmark'),

]

