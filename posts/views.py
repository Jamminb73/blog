from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from .forms import BlogForm

# Create your views here.

def posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get( 'page' )
    paged_posts = paginator.get_page(page)
    context = {'posts': paged_posts}
    return render(request, 'posts/posts.html', context)

@login_required
def post_create(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogForm
        return redirect('/posts')
    context = {'form': form}
    return render(request, 'posts/form.html', context)

def post_detail(request, post_id):
    postdetail = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': postdetail})

@login_required
def post_update(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    if obj.user != request.user:
        return redirect('posts')
    else:
        obj.user = request.user
        form = BlogForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('posts')
        context = {'form': form, "title": f"Update {obj.title}"}
        return render(request, 'posts/form.html', context)

@login_required
def post_delete(request, post_id):
    postdetail = get_object_or_404(Post, pk=post_id)
    if postdetail.user != request.user:
        return redirect('home')
    if request.method == "POST":
        postdetail.delete()
        return redirect('posts')
    context = {'post':postdetail}
    return render(request, 'posts/delete.html', context)
