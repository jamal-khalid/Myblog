from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post,BlogPost
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def Bloghome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render (request , 'blog/bloghome.html',context)


def blogpost(request ,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views+1
    post.save()

    comments=BlogPost.objects.filter(post=post,parent=None)
    replies=BlogPost.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context={'post':post , 'comments':comments,'user':request.user ,'replyDict':replyDict}
    return render (request , 'blog/blogpost.html',context)

def PostComment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')

        user =request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(sno=postSno)
        replySno=request.POST.get('replySno')

        if replySno=='':


            comment=BlogPost(comment=comment , user=user , post=post)
            comment.save()
            messages.success(request,'You comments has been post Successfully')

        else:
            parent=BlogPost.objects.get(sno=replySno)
            comment=BlogPost(comment=comment , user=user , post=post , parent=parent)
            comment.save()
            messages.success(request,'You reply has been post Successfully')

    return redirect(f'/blog/{post.slug}')