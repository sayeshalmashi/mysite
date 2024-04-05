from django.shortcuts import render,get_object_or_404

def blog_view(request):
  return render(request,'blog/blog-home.html')

def blog_single(request,pid):
  post= get_object_or_404(Post,pk=pid)
  context={'post':post}
  return render(request,'blog/blog-single.html',context)
