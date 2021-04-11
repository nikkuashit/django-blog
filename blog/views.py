from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import BlogForm
# Create your views here.


@login_required(login_url='/auth/signin')
def landingPage(request):
    blogs = Blog.objects.order_by('-created_on')
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)


@login_required(login_url='/auth/signin')
def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            userid = request.user
            print('*'*90)

            print(userid)

            new_blog = Blog(
                title=request.POST['title'], descreption=request.POST['descreption'], author=userid)
            new_blog.save()
            return redirect('home')
    else:
        form = BlogForm()

    form = BlogForm

    context = {'form': form}
    return render(request, 'blog/blog_form.html', context)
