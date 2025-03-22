
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from account.models import User

@login_required
def bookmarks_list(request):
    bookmarks = User.objects.get(pk=request.user.pk).bookmarks.all()
    return render(request, 'blog/bookmark.html', {'bookmarks' : bookmarks})

@login_required
def bookmark_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.bookmarks.remove(request.usser)
    return redirect('blog:bookmark-list')


@login_required
def toggle_bookmark(request, pk ):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmarks.filter(id=request.user.id).exiese():
        post.bookmarks.remove(request.user)

    else:
      post.bookmarks.add(request.user)
      return redirect('blog:post-detail', pk=post.pk)