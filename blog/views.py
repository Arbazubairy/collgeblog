from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def bloghome(request):
    allposts=Post.objects.all()
    context={'allposts':allposts}
    return render(request,'bloghome.html',context)

def blogpost(request,slug):
    slug=slug
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    context={'post':post,'comments':comments,'replies':replies}
    return render(request,'blogpost.html',context)

def blogcomments(request):
    if request.method == "POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentsno=request.POST.get("parentsno")
        parent=BlogComment.objects.get(blogsno=parentsno)
        if parent == "":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
        else:
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
    return redirect(f"/blog/{post.slug}")