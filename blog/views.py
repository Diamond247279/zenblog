from django.shortcuts import render

# Create your views here.
def homepage(request):
    context={
        'title':'homepage'
    }
    return render(request,'blog/index.html',context)

def about(request):
    context={
        'title':'about'
    }
    return render(request,'blog/about.html',context)

def contact(request):
    context={
        'title':'contact'
    }
    return render(request,'blog/contact.html',context)

def category(request):
    context={
        'title':'category'
    }
    return render(request,'blog/category.html',context) 
    
def search(request):
    context={
        'title':'search'
    }
    return render(request,'blog/search-result.html',context) 
    
def single(request):
    context={
        'title':'single'
    }
    return render(request,'blog/single-post.html',context) 
