from django.shortcuts import render, redirect
from .models import Post, Comments, Like
from django.contrib.auth.models import User


def blog_grid(request):
    try:
        obj = Post.objects.all()
        return render(request, 'blog.html', {'obj': obj})
    except:
        return render(request, 'blog.html', {'obj': obj})


def blog_details(request, pk):
    single_blogs = Post.objects.get(id=pk)
    print(single_blogs)
    obj7 = Post.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        Comments.objects.create(name=name, email=email, website=website, message=message,
                                commented_in_id=single_blogs.id)
        obj6 = Comments.objects.filter(commented_in_id=single_blogs.id)
        print(obj6)
        return render(request, 'single.html', {'obj5': single_blogs, 'obj6': obj6, 'obj7': obj7})
    else:
        obj6 = Comments.objects.filter(commented_in_id=single_blogs.id)
        print(obj6, 'return1')
        return render(request, 'single.html', {'obj5': single_blogs, 'obj6': obj6, 'obj7': obj7})


def post_like(request, pk):
    single_blogs = Post.objects.get(id=pk)
    obj7 = Post.objects.all()
    obj6 = Comments.objects.filter(commented_in_id=single_blogs.id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return render(request, 'single.html', {'obj5': single_blogs, 'obj6': obj6, 'obj7': obj7})

    # return redirect('Blog_app:blog_details')


def blog_post(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        return render(request, 'blog_post.html')
    else:
        author_name = request.POST.get('author_name')
        title = request.POST.get('title')
        date = request.POST.get('date')
        image = request.FILES['image']
        category = request.POST.get('category')
        description = request.POST.get('description')
        Post.objects.create(author_name=author_name, title=title, date=date, image=image, category=category,
                            description=description, user_id=user.id)
        return redirect('Blog_app:blog_grid')


def personal_blog(request):
    try:
        user = User.objects.get(id=request.user.id)
        obj9 = Post.objects.filter(user_id=user.id)
        return render(request, 'personal_blogs.html', {'obj9': obj9})
    except:
        return render(request, 'personal_blogs.html', {'obj9': obj9})


def blog_delete(request, pk):
    Post.objects.filter(id=pk).delete()
    return redirect('Blog_app:blog_grid')


def blog_update(request, pk):
    if request.method == 'GET':
        single_blogs = Post.objects.get(id=pk)
        return render(request, 'blog_update.html', {'obj8': single_blogs})
    else:
        author_name = request.POST.get('author_name')
        title = request.POST.get('title')
        date = request.POST.get('date')
        image = request.FILES['image']
        category = request.POST.get('category')
        description = request.POST.get('description')
        user = User.objects.get(id=request.user.id)
        obj55 = Post.objects.get(id=pk)
        obj55.author_name = author_name
        obj55.title = title
        obj55.date = date
        obj55.image = image
        obj55.category = category
        obj55.description = description
        obj55.user_id = user.id
        obj55.save()
        return redirect('Blog_app:blog_grid')
