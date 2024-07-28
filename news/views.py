from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    posts = Post.objects.all().order_by('-created_at')
    total_news = posts.count()
    for post in posts:
        post.short_text = ' '.join(post.text.split()[:20])
    return render(request, 'news/news_list.html', {'posts': posts, 'total_news': total_news})

def news_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'news/news_detail.html', {'post': post})
