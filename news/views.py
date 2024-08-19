from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

def news_list(request):
    posts = Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')
    paginator = Paginator(posts, 10)  # 10 новостей на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {'page_obj': page_obj})

def news_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'news/news_detail.html', {'post': post})

def news_search(request):
    news_filter = PostFilter(request.GET, queryset=Post.objects.filter(post_type=Post.NEWS))
    return render(request, 'news/news_search.html', {'filter': news_filter})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author  # Если пользователь авторизован как автор
        if 'news' in self.request.path:
            post.post_type = Post.NEWS
        elif 'articles' in self.request.path:
            post.post_type = Post.ARTICLE
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news/post_confirm_delete.html'
    success_url = reverse_lazy('news_list')