from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from itertools import chain
from django.contrib import messages
import itertools
from .models import *
from django.db.models import Q



@login_required(login_url='login')
def intrest_page(request):
    intr=intrest.objects.all()

    followig_user=request.user.id
    a="#Article"
    b="#Book"
    c="#Case Study"
    d="#Education"
    e="#Interviews"
    f="#Market Research"
    g="#Observation"
    h="#Poem"
    i="#Survey"
    j="#Work & Business"
    
 
    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=a).first():
         button_texta = 'Unfollow'
    else:  
        button_texta = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=b).first():
         button_textb = 'Unfollow'
    else:  
        button_textb = 'Follow'	  
    
     
    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=c).first():
         button_textc = 'Unfollow'
    else:  
        button_textc = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=d).first():
         button_textd = 'Unfollow'
    else:  
         button_textd = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=e).first():
         button_texte = 'Unfollow'
    else:  
        button_texte = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=f).first():
         button_textf = 'Unfollow'
    else:  
        button_textf = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=g).first():
         button_textg = 'Unfollow'
    else:  
        button_textg = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=h).first():
         button_texth = 'Unfollow'
    else:  
        button_texth = 'Follow'	      


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=i).first():
         button_texti = 'Unfollow'
    else:  
        button_texti = 'Follow'	 


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=j).first():
         button_textj = 'Unfollow'
    else:  
        button_textj = 'Follow'	                   



    return render(request,"intrest.html",{"intr":intr,"button_texta":button_texta,"button_textb":button_textb,"button_textc":button_textc,
                                          "button_textd":button_textd,"button_texte":button_texte,"button_textf":button_textf,
                                          "button_textg":button_textg,"button_texth":button_texth,"button_texti":button_texti,"button_textj":button_textj})




def intrest_create(request):
    if request.method == 'POST':
        intr = request.POST['intr']
        int=intrest(
            intr=intr
        )
        int.save()
        return redirect("index")
         
        
       


@login_required(login_url='login')
def index(request):
    
    usr=User.objects.all()

    choose=intrest_followers.objects.all()
    user_following_list = []
    feed = []
   
    intr_following_list=[]
    intr=[]

    us=request.user


    user_followers = len(friend_request.objects.filter(to_user=us))
    user_following = len(friend_request.objects.filter(from_user=us))   

    


    user_following = intrest_followers.objects.filter(following_user=request.user)


    for users in user_following:
        intr_following_list.append(users.topic)

    for usernames in intr_following_list:
        feed_lists = Post.objects.filter(intr_id=usernames) 

        intr.append(feed_lists,)
    

    user_following = friend_request.objects.filter(from_user__username=request.user.username)


    for users in user_following:
        user_following_list.append(users.to_user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(creater=usernames)  
        
        feed.append(feed_lists,)

    

    posts = list(chain(*intr))
 

   
    frd=friend.objects.all()
    pending=friend_request.objects.all()


    
    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user',flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]


    intrests = []
    if request.user.is_authenticated:
        followings = intrest_followers.objects.filter(following_user=request.user).values_list('topic', flat=True)
        intrests = intrest.objects.exclude(pk__in=followings).exclude().order_by("?")[:6]
    

    intr=intrest.objects.all()

    


    followig_user=request.user.id
    a="#Article"
    b="#Book"
    c="#Case Study"
    d="#Education"
    e="#Interviews"
    f="#Market Research"
    g="#Observation"
    h="#Poem"
    i="#Survey"
    j="#Work & Business"
    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=a).first():
         button_texta = 'Unfollow'
    else:  
        button_texta = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=b).first():
         button_textb = 'Unfollow'
    else:  
        button_textb = 'Follow'	  
    
     
    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=c).first():
         button_textc = 'Unfollow'
    else:  
        button_textc = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=d).first():
         button_textd = 'Unfollow'
    else:  
         button_textd = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=e).first():
         button_texte = 'Unfollow'
    else:  
        button_texte = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=f).first():
         button_textf = 'Unfollow'
    else:  
        button_textf = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=g).first():
         button_textg = 'Unfollow'
    else:  
        button_textg = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=h).first():
         button_texth = 'Unfollow'
    else:  
        button_texth = 'Follow'	      


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=i).first():
         button_texti = 'Unfollow'
    else:  
        button_texti = 'Follow'	 


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=j).first():
         button_textj = 'Unfollow'
    else:  
        button_textj = 'Follow'	                   

    return render(request, "network/index.html",{
        "posts": posts,
        'pending':pending,
        "suggestions": suggestions,  
        "user_followers":user_followers,    
        "page": "all_posts",
        "intrests":intrests,
        'profile': False,
         "frd":frd,
         "usr":usr.count(),  
         "intr":intr,"button_texta":button_texta,"button_textb":button_textb,"button_textc":button_textc,
                                          "button_textd":button_textd,"button_texte":button_texte,"button_textf":button_textf,
                                          "button_textg":button_textg,"button_texth":button_texth,"button_texti":button_texti,"button_textj":button_textj,"choose":choose,
       
    })


def article_list_by_tag(request, tag):
    post = Post.objects.filter(tages_n=tag)
    context = {
        'post': post,
        'tag': tag,
        
    }
    return render(request, 'article_list.html', context)



# class postDetailView(HitCountDetailView):
#     model = Post
#     template_name = "network/index.html"
#     slug_field = "slug"
#     count_hit = True

@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["firstname"]
        if fname == None:
            fname = "none"

        lname = request.POST["lastname"]
        if lname == None:
            lname = "none"
        profile = request.FILES.get("profile")
   
       
        cover = request.FILES.get('cover')
       

        # Ensure password matches confirmation
        password = request.POST["password"]
        # confirmation = request.POST["confirmation"]
        # if password != confirmation:
        #     return render(request, "network/register.html", {
        #         "message": "Passwords must match."
        #     })

        # Attempt to create new user
        try: 
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            if profile is not None:
                user.profile_pic = profile
            else:
                user.profile_pic = "../static/propic.jpg"
            user.cover = cover           
            user.save()
            Follower.objects.create(user=user)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("intrest_page"))
    else:
        return render(request, "network/register.html")


@login_required(login_url='login')
def profile(request, username):
    user = User.objects.get(id=username)
    all_posts = Post.objects.filter(creater=user).order_by('-date_created')
    frd = friend.objects.filter()
    rqst=friend_request.objects.filter()

    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    posts = paginator.get_page(page_number)
    
    

    to=request.user.id
    fr=username

    if friend_request.objects.filter(from_user__id=to, to_user__id=fr,stat='following').first():
         button_text = 'Unfollow'
    else:  
        button_text = 'Follow'

    user_followers = len(friend_request.objects.filter(to_user=username))
    user_following = len(friend_request.objects.filter(from_user=username))   
    intrests=intrest.objects.all().order_by("?")[:5]


     
    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6] 
   
    return render(request, 'network/profile.html', {
        "username": user,
        "posts": posts,
        'button_text': button_text,
        "posts_count": all_posts.count(),
        "rqst":rqst,
        "page": "profile",
        "suggestions": suggestions,      
        "intrests":intrests,
        "frd":frd,
        'user_followers': user_followers,
        'user_following': user_following,
       
    })

def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')



def saved(request):
    if request.user.is_authenticated:
        all_posts = Post.objects.filter(savers=request.user).order_by('-date_created')

        paginator = Paginator(all_posts, 10)
        page_number = request.GET.get('page')
        if page_number == None:
            page_number = 1
        posts = paginator.get_page(page_number)

        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
        return render(request, "network/index.html", {
            "posts": posts,
            "suggestions": suggestions,
            "page": "saved"
        })
    else:
        return HttpResponseRedirect(reverse('login'))
        
def intrest_create_post(request,pk):
    intr = intrest.objects.get(id=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        categories=request.POST.get('categories')
        title=request.POST.get('title')
     
        doc=request.FILES.get('doc')
        status=request.POST.get('status')
        tages_n=request.POST.get('tages_n')
        if tages_n == "":
            tages_n = "True"
        if status == None:
            status = "nsale"
        Product_Price=request.POST.get('Product_Price')
        vedio=request.FILES.get('vedio')  
        if Product_Price=="":
            Product_Price=None

        post = Post(creater=request.user,intr_id=intr, content_text=text,title=title,categories=categories,tages_n=tages_n, content_image=pic,status=status,Product_Price=Product_Price,posts_type="intrest_post",doc=doc,vedio=vedio)
        post.save()
        return redirect("topicpage",pk)    


@csrf_exempt
def user_create_post(request,pk):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        categories=request.POST.get('categories')
        title=request.POST.get('title')
     
        doc=request.FILES.get('doc')
        status=request.POST.get('status')
        tages_n=request.POST.get('tages_n')
        if tages_n == "":
            tages_n = "True"
        if status == None:
            status = "nsale"
        Product_Price=request.POST.get('Product_Price')
        vedio=request.FILES.get('vedio')  
        if Product_Price=="":
            Product_Price=None

        post = Post(creater=request.user, content_text=text,title=title,categories=categories,tages_n=tages_n, content_image=pic,status=status,Product_Price=Product_Price,posts_type="user_post",doc=doc,vedio=vedio)
        post.save()
        return redirect("index")


@csrf_exempt
def edit_post(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        img_chg = request.POST.get('img_change')
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        try:
            post.content_text = text
            if img_chg != 'false':
                post.content_image = pic
            post.save()
            
            if(post.content_text):
                post_text = post.content_text
            else:
                post_text = False
            if(post.content_image):
                post_image = post.img_url()
            else:
                post_image = False
            
            return JsonResponse({
                "success": True,
                "text": post_text,
                "picture": post_image
            })
        except Exception as e:
    
            return JsonResponse({
                "success": False
            })
    else:
            return HttpResponse("Method must be 'POST'")

@csrf_exempt
def like_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
          
            try:
                post.likers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unlike_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
          
            try:
                post.likers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def save_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            try:
                post.savers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unsave_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            try:
                post.savers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def follow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
          
            try:
                (follower, create) = Follower.objects.get_or_create(user=user)
                follower.followers.add(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unfollow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
        
            try:
                follower = Follower.objects.get(user=user)
                follower.followers.remove(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))






def pageindex(request):
    all_posts = Post.objects.all().order_by('-date_created')
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    pagepost = paginator.get_page(page_number)
    followings = []
    suggestions = []  
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:4]
    return render(request, "pageindex.html", {
        "posts": pagepost,
        "suggestions": suggestions, 
        "page": "all_posts",
        'profile': False
    })

def pag(request,pk):

    pag=page.objects.all()
    pge=invited.objects.all()
    all_pages=page.objects.order_by("?")[:4]
    intrests=intrest.objects.all().order_by("?")[:5]
   

    context={
        "pag":pag,
       "pge":pge,
       "all_pages":all_pages,
       "intrests":intrests
       }
   
    
    
    return render(request,"page.html",context) 



def mypage(request,pk):
    
    pag=page.objects.all()
    return render(request,"mypage.html",{"pag":pag,})  




def page_registration(request,pk):
    rgs=User.objects.get(id=pk)
    suggestions = []
    follower=False
   
    return render(request,"page_registration.html",{"rgs":rgs,
    })

    
        

@csrf_exempt
def page_creation(request,pk):
    if request.method == 'POST':
        
        creater=request.user
        pagename = request.POST.get('pagename')
        website = request.FILES.get('website')
        username=request.POST.get('username')
        category= request.POST.get('category')
        emial=request.POST.get('emial')
        image=request.FILES.get('image')

        
        pag = page(creater=creater, pagename=pagename, website=website,emial=emial,category=category,image=image,username=username)
           
        pag.save()
        return redirect("pag",pk)

@login_required(login_url='login')
def pageprofile(request,pageid):
    pro=page.objects.get(id=pageid)
    posts = Post.objects.filter(page_id=pageid).order_by('-date_created')
    followings = []
    suggestions = []
    follower=False
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

        if request.user in Follower.objects.get(user=pro.creater).followers.all():
            follower = True

    follower_count = Follower.objects.get(user=pro.creater).followers.all().count()
    following_count = Follower.objects.filter(followers=pro.creater).count()        
    # suggestions = User.objects.all()
    req=invite_request.objects.all
    return render(request,"pageprofile.html",{"pro":pro,"posts":posts,"pag":pag,'req':req,
    "posts_count": posts.count(),
    "suggestions":suggestions,
    "is_follower": follower,
    "follower_count": follower_count,
        "following_count": following_count
    })  

def pagepost(request,pk):
    pg = page.objects.get(id=pk)
    return render(request,"pagepost.html",{"pg":pg})   

@login_required(login_url='login')
@csrf_exempt
def create_pagepost(request,pageid):
    pag = page.objects.get(id=pageid)
    if request.method == 'POST':
        content_text = request.POST.get('content_text')
        content_image = request.FILES.get('content_image')
        status=request.POST.get('status')
        if status == None:
            status = "nsale"
        Product_Price=request.POST.get('Product_Price')
        if Product_Price == "":
            Product_Price = None
        page_name=request.POST.get("page_name")
        vedio=request.FILES.get('vedio')  
        doc=request.FILES.get('doc')
        categories=request.POST.get('categories')
        title=request.POST.get('title')
        
        
    
        post = Post(creater=request.user,page_id=pag,categories=categories,content_text=content_text,title=title, content_image=content_image,page_name=page_name,status=status,Product_Price=Product_Price,posts_type="page_post",vedio=vedio,doc=doc)
        post.save()
        return redirect("pageprofile",pageid)  



        

def cart(request):
    return render(request,"cart.html")



def checkout(request):
    return render(request,"checkout.html")



@login_required(login_url='signin')
def category(request,id):
    category = Category.objects.get(id=id)
    product = Product.objects.filter(Category_Name=category)

    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        
        
    }
    return render(request,'shop-full.html',context)



@login_required(login_url='signin')
def show_all(request):
   
    product = Product.objects.all()
    category = Category.objects.all()
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 

    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
               
    }
    return render(request,'shop-full.html',context)

@login_required(login_url='login')
def product_detail(request,id):
    product=Post.objects.filter(id=id)
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total= 0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 

    grand_total =  sub_total + shipping
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
    }

    return render(request,'product-detail.html',context) 



def add_cart(request,id):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        product=Post.objects.get(id=id)

        
        

        ct=Cart(user=user,product=product,product_qty="1")
        ct.save()
        return redirect('cart')


@login_required(login_url='signin')
def cart(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping

    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        
    }


    return render(request,'cart.html',context)    

def zip(request):
    if request.method=='POST':
        zipcode=request.POST['zip']
        if Zip.objects.filter(zip_code=zipcode).exists():
            messages.info(request, 'Delery avilable')
            return redirect('cart') 
        else:
            messages.info(request, 'Delery is not avilable')
            return redirect('cart')


def remove_cart(request,id):
    crt=Cart.objects.get(id=id)
    crt.delete()
    return redirect('cart')

def remove_cart_all(request):
    crt=Cart.objects.filter(user=request.user)
    crt.delete()
    return redirect('cart')
    

@login_required(login_url='signin')
def checkout(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    ship = Shipping_address.objects.filter(user=request.user)

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    orderitem = Order_Item.objects.filter(user=request.user)
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)



    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'ship'    :   ship,
        'orderitem'  : orderitem,
        'shipadd'  : shipadd,
        
    }

    return render(request,'checkout.html',context)   


@login_required(login_url='signin')
def shipping_address(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        if Shipping_address.objects.filter(user=request.user).exists():
            ship1 =Shipping_address.objects.get(user=request.user)
            ship1.user=user
            ship1.Full_name = request.POST['fullname']
            ship1.Phone = request.POST['phone']
            ship1.House = request.POST['house']
            ship1.Area = request.POST['area']
            ship1.Landmark = request.POST['landmark']
            ship1.Town = request.POST['town']
            ship1.State = request.POST['state']
            ship1.Zip = request.POST['zip']
            ship1.save()
            return redirect('checkout')
        else:
            ship=Shipping_address()
            ship.user=user
            ship.Full_name = request.POST['fullname']
            ship.Phone = request.POST['phone']
            ship.House = request.POST['house']
            ship.Area = request.POST['area']
            ship.Landmark = request.POST['landmark']
            ship.Town = request.POST['town']
            ship.State = request.POST['state']
            ship.Zip = request.POST['zip']
            ship.save()
            return redirect('checkout')
        


def place_order(request,id):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)

        ship=Shipping_address.objects.get(id=id)
        
        neworder= Order()

        neworder.user = user
        neworder.shipping_address = ship

        neworder.payment_mode = request.POST['payment']

        cart = Cart.objects.filter(user=request.user)
        crt_total_price = 0

        for i in cart:
            crt_total_price = crt_total_price +  i.product_qty * i.product.Product_Price 


        neworder.total_price = crt_total_price

        trackno = 'ananthu'+str(random.randint(1111111,9999999))

        while Order.objects.filter(tracking_no=trackno ) is None:
            trackno = 'ananthu'+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            Order_Item.objects.create(
                user = request.user,
                order = neworder,
                product = item.product,
                price  = item.product.Product_Price,
                quanty = item.product_qty

            )
        Cart.objects.filter(user=request.user).delete()

        messages.success(request,"Your order has been placed successfully")

        return redirect ('my_order')
               
    

@login_required(login_url='signin')
def dashboard(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    ship = Shipping_address.objects.filter(user=request.user)

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)



    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'ship'    :   ship,
        'orderitem'  : orderitem,
        'shipadd'  : shipadd,
        'order_count' : order_count,
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='signin')
def dashboard_profile(request): 
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
    }

    return render(request,'dash-my-profile.html',context)


@login_required(login_url='signin')
def dash_edit_profile(request):
    
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
    }


    return render(request,'dash-edit-profile.html',context)


@login_required(login_url='signin')
def edit(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        pho=Member.objects.get(user=request.user)
        pho.phone=request.POST['phone']
        user.save()
        pho.save()
        return redirect('dash_edit_profile')     

@login_required(login_url='signin')
def dash_address_book(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 

    ship = Shipping_address.objects.filter(user=request.user)
    address = ""
    reg = ""
    for i in ship:
        address = str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State) +" , " + str(i.Zip)
        reg = str(i.Town)+" , " + str(i.State) 

    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'address':address,
        'reg':reg,
        'ph' :ph,

       
        'order_count':order_count,
    }
    return render(request,'dash-address-book.html',context)

@login_required(login_url='signin')
def track_order(request):

    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()


    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'order_count' :order_count,
        
    }
    return render(request,'dash-track-order.html',context)


def my_order(request):

    sub_total=0 
    grand_total = 0
    shipping =50
    

    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
      
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
      
        'order_count':order_count,
        'orderitem' :orderitem,
    }
    return render(request,'dash-my-order.html',context) 




def manage_order(request,id):  
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    ship = Shipping_address.objects.filter(user=request.user)
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)
        fullname =str(i.Full_name)
    
    order_count = orderitem.count()
    category = Category.objects.all()
    manageorder = Order_Item.objects.get(id=id)
    total=0
    total=(manageorder.price *manageorder.quanty) + shipping
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
        'orderitem' :orderitem,
        'manageorder' :manageorder,
        'total' :total,
        'shipadd' :shipadd,
        'fullname' : fullname,
    }
    return render(request,'dash-manage-order.html',context) 



@login_required(login_url='signin')
def admin_dash(request):
    if not request.user.is_staff:
        return redirect('signin')
    return render(request,'administrator/index.html') 

@login_required(login_url='signin')
def dash_category(request):
    category=Category.objects.all()
    context={
        'category':category,

    }
    return render(request,'administrator/category.html',context)

@login_required(login_url='signin')
def add_category(request):
    if request.method=='POST':
        cat=Category()
        cat.Category_Name = request.POST['category']
        cat.save()
        return redirect('dash_category')

@login_required(login_url='signin')
def del_category(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return redirect('dash_category')




@login_required(login_url='signin')
def dash_product(request):
    cat=Category.objects.all()
    context ={
        'cat' :cat,

         }

    return render(request,'administrator/products.html',context)




@csrf_exempt
def edit_product(request,id):
    
    cat=Category.objects.all()
    product=Product.objects.get(id=id)
    context ={
        'cat' :cat,
        'product' :product,
         }
        
    return render(request,'administrator/edit_product.html',context)


@csrf_exempt
def edit_pro(request,id):

    if request.method=='POST':
        c = request.POST['cat']
        cat=Category.objects.get(id=c)
        pro=Product.objects.get(id=id)
       
        pro.Category_Name = cat
        
        pro.Product_Name = request.POST['pname']
        pro.Product_Description = request.POST['desp']
        pro.Product_Price = request.POST['price']
        pro.Product_Delprice = request.POST['delprice']
        if len(request.FILES) != 0:
            if len(pro.Product_Image) > 0  :
                os.remove(pro.Product_Image.path)
            pro.Product_Image = request.FILES['file']
            
        pro.save()
        return redirect('show_product')



@login_required(login_url='signin')
def show_product(request):

    product=Product.objects.all()
    context= {
        'product' : product,

    }

    return render(request,'administrator/show_product.html',context)

@login_required(login_url='signin')
def show_order(request):
    order = Order.objects.all()
    context = {
        'order' :order,
    }
    return render(request,'administrator/show_order.html',context)

@login_required(login_url='signin')
def status(request,id):
    if request.method=='POST':
        order = Order.objects.get(id=id)
        
        order.status = request.POST['st']
        order.save()
        return redirect('show_order')
          



@login_required(login_url='signin')
def show_order_product(request,id):
    items=Order_Item.objects.filter(order=id)
    order =Order.objects.get(id=id)
    context={
       'items' : items,
       'order' :order,
    }
    return render(request,'administrator/show_order_product.html',context)   



# def show_user(request):

#     users = User.objects.all()
#     return render(request,'administrator/show_users.html',{'users':users})   


def user_carts(request,id):
    us = User.objects.get(id=id)
    
    carts=Cart.objects.filter(user=us)
    context = {
        'carts' : carts,
    }
    

    return render(request,'administrator/view_carts.html',context)  


# def logout(request):
#     request.session["uid"] = ""
#     auth.logout(request)
#     return redirect('index')


# def add_product(request):
#      if request.method == 'POST':
#         Product_Name = request.POST.get('Product_Name')
#         Product_Image = request.FILES.get('Product_Image')
#         Product_Price= request.POST.get('Product_Price')
#         Product_Description=request.POST.get('Product_Description')
#         date_created=request.POST.get('date_created')
#         try:
#             sel = Product.objects.create(creater=request.user, Product_Name=Product_Name, Product_Image=Product_Image,Product_Price=Product_Price,Product_Description=Product_Description,
#             date_created=date_created)
#             return HttpResponseRedirect(reverse('index'))
#         except Exception as e:
#             return HttpResponse(e)
#      else:
#         return HttpResponse("Method must be 'POST'")


# def dash(request):
#     return render(request,"")    


def edit_profile(request,pk):
    profile=User.objects.get(id=pk)
    return render(request,"edit_profile.html",{"profile":profile})

@csrf_exempt
def edit_pr(request,pk):
    if request.method=='POST':
        profile=User.objects.get(id=pk)
        profile.first_name=request.POST['first_name']
        profile.last_name=request.POST['last_name']
        profile.username=request.POST['username']
        profile.email=request.POST['email']
        profile.profile_pic=request.FILES.get("profile")
        profile.cover=request.FILES.get('cover')

        profile.save()
        return redirect('profile',pk)   




def edit_page(request,pk):
    profile=page.objects.get(id=pk)
    return render(request,"edit_page.html",{"profile":profile})      


@csrf_exempt
def edit_pages(request,pk):
    if request.method=='POST':
        profile=page.objects.get(id=pk)
        profile.pagename=request.POST['pagename']
        profile.category=request.POST['category']
        profile.emial=request.POST['emial']
        profile.cover=request.FILES.get("cover")
        profile.image=request.FILES.get("image")
       

        profile.save()
        return redirect('/')     

def search(request):
    template = 'search.html'
    query = request.GET.get('q')

    

    # Search for pages
    pages = page.objects.filter(Q(pagename__icontains=query))
    page_count = pages.count()

    # Search for interests
    interests = intrest.objects.filter(Q(intrest_name__icontains=query))
    interest_count = interests.count()


      # Search for users
    users = User.objects.filter(Q(username__icontains=query))
    user_count = users.count()

    # Search for posts
    posts = Post.objects.filter(Q(creater__username__icontains=query))
    post_count = posts.count()

    # Display a message if no results were found
    if user_count == 0 and post_count == 0:
        message = 'No results found for "{}".'.format(query)
    else:
        message = 'Showing results for "{}".'.format(query)
 
    # Combine search results and remove duplicates
    results = list(itertools.chain(users, pages, interests,posts))
    results = list(set(results))

    # Hide username field if no matching users found
    hide_username = user_count == 0

    context = {
        'query': query,
        'users': users,
        'user_count': user_count,
        'posts': posts,
        'post_count': post_count,
        'message': message,
        'results': results,
        'hide_username': hide_username,
    }
    return render(request, template, context) 

# def search(request):
#     template='search.html'

#     query = request.GET['q']
   
#     data = query

#     count = {}
#     results = {}
#     results['posts']= User.objects.none()
#     queries = data.split()
#     for query in queries:
#         results['posts'] = results['posts'] | User.objects.filter(username__icontains=query)
#         count['posts'] = results['posts'].count()


   

#     count4 = {}
#     queries4 = data.split()
#     results4 = {}
#     results4['posts'] = page.objects.none()
#     for query4 in queries:
#         results4['posts'] = results4['posts'] | page.objects.filter(pagename__icontains=query4)
#         count4['posts'] = results4['posts'].count()

#     count5 = {}
#     queries5 = data.split()
#     results5 = {}
#     results5['posts'] = intrest.objects.none()
#     for query5 in queries:
#         results5['posts'] = results5['posts'] | intrest.objects.filter(intrest_name__icontains=query5)
#         count5['posts'] = results5['posts'].count()
        

#     files = itertools.chain(results['posts'],results4['posts'],results5['posts'])
#     result = []
#     for i in files:
#         if i not in result:
#             result.append(i)    

#     paginate_by=2
#     username = request.user.username
    
   
#     person = User.objects.get(username = username)
    

	
#     context={ 'files':result }
#     return render(request,template,context)

# def search(request):
#     query = request.GET.get('q')
#     results = search_item.objects.filter((username__icontains=query) | (pagename__icontains=query) | (intrest_name__icontains=query))
#     context = {
#         'results': results,
#     }
#     return render(request, 'search.html', context)




def intrest_follow(request,pk):
    followig_user=request.user
    topic=intrest.objects.get(id=pk)
    intr_follow=intrest_followers(following_user=followig_user,topic=topic)
    intr_follow.save()
    return redirect("intrest_page")



def intrest_unfollow(request,pk):
    followig_user=request.user
    topic=pk
    s=intrest_followers.objects.filter(following_user=followig_user,topic=topic)
    s.delete()
    return redirect("intrest_page")


def filter_intrest_follow(request,pk):
    followig_user=request.user
    topic=intrest.objects.get(id=pk)
    intr_follow=intrest_followers(following_user=followig_user,topic=topic)
    intr_follow.save()
    return redirect("index")



def filter_intrest_unfollow(request,pk):
    followig_user=request.user
    topic=pk
    s=intrest_followers.objects.filter(following_user=followig_user,topic=topic)
    s.delete()
    return redirect("index")


def intrest_follow_topicpage(request,pk):
    followig_user=request.user
    topic=intrest.objects.get(id=pk)
    intr_follow=intrest_followers(following_user=followig_user,topic=topic)
    intr_follow.save()
    return redirect("topicpage",pk)



def intrest_unfollow_topicpage(request,pk):
    followig_user=request.user
    topic=pk
    s=intrest_followers.objects.filter(following_user=followig_user,topic=topic)
    s.delete()
    return redirect("topicpage",pk)
    


def sent_friend_request(request,userid):
    from_user=request.user
    to_user=User.objects.get(id=userid)
    frequest =friend_request(from_user=from_user,to_user=to_user,stat="following")
    frequest.save()
    return redirect("profile",userid)
    
    


def accept_friend_request(request,requestid):
    request=friend_request.objects.get(id=requestid)

    to=request.to_user
    fr=request.from_user
    gg=friend(
        to=to,
        fr=fr,
    )
    gg.save()
   
    
    # request.to_user.frdz.add(request.from_user)
    # request.from_user.frdz.add(request.to_user)
    request.delete()
    return HttpResponse("/")
    
    

  


def userfriends(request,id):
    frd = friend.objects.filter()
    return render(request,"userfriends.html",{"frd":frd})    


#invite


def sent_invite_request(request,userid,id):
    from_user=request.user
    pages=page.objects.get(id=id)
    to_user=User.objects.get(id=userid)
    frequest =invite_request(from_user=from_user,to_user=to_user,pages=pages)
    frequest.save()
    messages.info(request, 'Invitation Request Sent Successfully..')
    
    return redirect("pageprofile",id)
    



def accept_invite_request(request,requestid,):
    request=invite_request.objects.get(id=requestid)

    to_user=request.to_user
    fr_user=request.from_user
    fr_pages=request.pages
    gg=invited(
       to_user=to_user,
       fr_user=fr_user,
       fr_pages=fr_pages 
    )
    gg.save()
    
   
    # request.to_user.frdz.add(request.from_user)
    # request.from_user.frdz.add(request.to_user)
    request.delete()

    return redirect("/")
    


def notification(request,nid):
    fr=friend_request.objects.all()
    inv=invite_request.objects.all()
    pag=page.objects.all()
    foll=Follower.objects.all()
    intrests=intrest.objects.all().order_by("?")[:5]

    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
   
    return render(request,"notification.html",{'fr':fr,"inv":inv,'pag':pag,"foll":foll,"suggestions":suggestions,"intrests":intrests})  



def userinviters(request,id):
    frd = invited.objects.filter()
    return render(request,"userfriends.html",{"frd":frd})     


def delete_inv(request,pk):
    delete=invite_request.objects.get(id=pk)
    delete.delete()
    messages.info(request, 'Invitation Request Deleted Successfully..')
    return redirect('/')



def delete_frd(request,pk):
    to=request.user.id
    fr=pk

    s=friend_request.objects.filter(from_user__id=to, to_user__id=fr,stat='following')
    s.delete()
   
    return redirect('profile',pk)



def delete_post(request,pk) :
    delete=Post.objects.get(id=pk)
    delete.delete()
    return redirect('/')   

def pages_accept_invites(request,pk):
    pge=invited.objects.all()
    return render(request,'pages_accept_invites.html',{'pge':pge})

def post_comment(request,pk):
    post=Post.objects.filter(id=pk)
    comment=Comment.objects.filter(post_id=pk)
    intrests=intrest.objects.all().order_by("?")[:5]
    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
    



    
    context = {
        'post'  : post, 
        'comment':comment,
        "suggestions":suggestions,
        "intrests":intrests
       
    }

    return render(request,'post_comment.html',context)



def commentz(request,userid):
    post=Post.objects.get(id=userid)
    commenter=request.user
    comment_content= request.POST.get('comment_content')
    cmd =Comment(post=post,commenter=commenter,comment_content=comment_content)
    cmd.save()
    return redirect("post_comment",userid)
        

def nsale_post_share(request,pk):
    post=Post.objects.filter(id=pk)
   



    
    context = {
        'post'  : post, 
     
       
    }

    return render(request,'nsale_post_share.html',context)       



def sale_post_share(request,pk):
    post=Post.objects.filter(id=pk)
   



    
    context = {
        'post'  : post, 
     
       
    }

    return render(request,'sale_post_share.html',context)          



def add_to_wish(requset,pk):
    usr=requset.user
    post=Post.objects.get(id=pk)
    wish=wishlist(usr=usr,post=post)
    wish.save()
    return redirect("index")







def wishlis(request,pk):
    wsh=wishlist.objects.all()
    intrests=intrest.objects.all().order_by("?")[:5]
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

    return render(request,'wishlist.html',{'wsh':wsh,"suggestions":suggestions,"intrests":intrests})


def delete_wishlist(request,pk):
    delete=wishlist.objects.get(id=pk)
    delete.delete()
    return redirect('wishlis',pk)  


def pdf_view(request):
    with open('E:\mypdf.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
    


def topicpage(request,pk):
    intr = intrest.objects.get(id=pk)
    posts = Post.objects.filter(intr_id=pk).order_by('-date_created')

    user_followers = len(intrest_followers.objects.filter(topic=pk))


    to=request.user.id
    fr=pk

    if intrest_followers.objects.filter(following_user=to, topic=fr).first():
         button_text = 'Unfollow'
    else:  
        button_text = 'Follow'


    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user',flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]


    intrests = []
    if request.user.is_authenticated:
        followings = intrest_followers.objects.filter(following_user=request.user).values_list('topic', flat=True)
        intrests = intrest.objects.exclude(pk__in=followings).exclude().order_by("?")[:6]
        
    

   
    return render(request,'topicpage.html',{'intr':intr,"posts": posts,"button_text":button_text,"user_followers":user_followers,"intrests":intrests, "suggestions": suggestions,   })


def new_post(request):
    usr=User.objects.all()
   
   

    intr_following_list=[]
    intr=[]

    us=request.user

   

    user_following = intrest_followers.objects.filter(following_user=request.user)


    for users in user_following:
        intr_following_list.append(users.topic)

    for usernames in intr_following_list:
        feed_lists = Post.objects.filter(intr_id=usernames).order_by('-date_created')

        intr.append(feed_lists,)
 
    

    posts = list(chain(*intr))
 

   
    frd=friend.objects.all()
    pending=friend_request.objects.all()


    
    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user',flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]


    intrests = []
    if request.user.is_authenticated:
        followings = intrest_followers.objects.filter(following_user=request.user).values_list('topic', flat=True)
        intrests = intrest.objects.exclude(pk__in=followings).exclude().order_by("?")[:6]
    
    


    intr=intrest.objects.all()


    followig_user=request.user.id
    a="#Article"
    b="#Book"
    c="#Case Study"
    d="#Education"
    e="#Interviews"
    f="#Market Research"
    g="#Observation"
    h="#Poem"
    i="#Survey"
    j="#Work & Business"
    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=a).first():
         button_texta = 'Unfollow'
    else:  
        button_texta = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=b).first():
         button_textb = 'Unfollow'
    else:  
        button_textb = 'Follow'	  
    
     
    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=c).first():
         button_textc = 'Unfollow'
    else:  
        button_textc = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=d).first():
         button_textd = 'Unfollow'
    else:  
         button_textd = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=e).first():
         button_texte = 'Unfollow'
    else:  
        button_texte = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=f).first():
         button_textf = 'Unfollow'
    else:  
        button_textf = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=g).first():
         button_textg = 'Unfollow'
    else:  
        button_textg = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=h).first():
         button_texth = 'Unfollow'
    else:  
        button_texth = 'Follow'	      


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=i).first():
         button_texti = 'Unfollow'
    else:  
        button_texti = 'Follow'	 


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=j).first():
         button_textj = 'Unfollow'
    else:  
        button_textj = 'Follow'	     

    return render(request, "new_post.html",{
        "posts": posts,
        'pending':pending,
        "suggestions": suggestions,      
        "page": "all_posts",
        "intrests":intrests,
        'profile': False,
         "frd":frd,
         "usr":usr.count(),  
         "intr":intr,"button_texta":button_texta,"button_textb":button_textb,"button_textc":button_textc,
                                          "button_textd":button_textd,"button_texte":button_texte,"button_textf":button_textf,
                                          "button_textg":button_textg,"button_texth":button_texth,"button_texti":button_texti,"button_textj":button_textj
       
    })


def user_posts(request):
    usr=User.objects.all()
    choose=intrest_followers.objects.all()
    user_following_list = []
    feed = []


   
    us=request.user

    user_following = friend_request.objects.filter(from_user__username=request.user.username)


    for users in user_following:
        user_following_list.append(users.to_user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(creater=usernames)  
        
        feed.append(feed_lists,)


    
 
    

    posts = list(chain(*feed))
 

   
    frd=friend.objects.all()
    pending=friend_request.objects.all()


    
    suggestions = []
    if request.user.is_authenticated:
        followings = friend_request.objects.filter(from_user=request.user).values_list('to_user',flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]


    intrests = []
    if request.user.is_authenticated:
        followings = intrest_followers.objects.filter(following_user=request.user).values_list('topic', flat=True)
        intrests = intrest.objects.exclude(pk__in=followings).exclude().order_by("?")[:6]
    
    intr=intrest.objects.all()


    followig_user=request.user.id
    a="#Article"
    b="#Book"
    c="#Case Study"
    d="#Education"
    e="#Interviews"
    f="#Market Research"
    g="#Observation"
    h="#Poem"
    i="#Survey"
    j="#Work & Business"
    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=a).first():
         button_texta = 'Unfollow'
    else:  
        button_texta = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=b).first():
         button_textb = 'Unfollow'
    else:  
        button_textb = 'Follow'	  
    
     
    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=c).first():
         button_textc = 'Unfollow'
    else:  
        button_textc = 'Follow'	


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=d).first():
         button_textd = 'Unfollow'
    else:  
         button_textd = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=e).first():
         button_texte = 'Unfollow'
    else:  
        button_texte = 'Follow'	   


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=f).first():
         button_textf = 'Unfollow'
    else:  
        button_textf = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=g).first():
         button_textg = 'Unfollow'
    else:  
        button_textg = 'Follow'	    


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=h).first():
         button_texth = 'Unfollow'
    else:  
        button_texth = 'Follow'	      


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=i).first():
         button_texti = 'Unfollow'
    else:  
        button_texti = 'Follow'	 


    if intrest_followers.objects.filter(following_user=followig_user, topic__intrest_name=j).first():
         button_textj = 'Unfollow'
    else:  
        button_textj = 'Follow'	     

    return render(request, "user_posts.html",{
        "posts": posts,
        'pending':pending,
        "suggestions": suggestions,      
        "page": "all_posts",
        "intrests":intrests,
        'profile': False,
         "frd":frd,
         "usr":usr.count(),  
          "intr":intr,"button_texta":button_texta,"button_textb":button_textb,"button_textc":button_textc,
                                          "button_textd":button_textd,"button_texte":button_texte,"button_textf":button_textf,
                                          "button_textg":button_textg,"button_texth":button_texth,"button_texti":button_texti,"button_textj":button_textj,"choose":choose,
       
    })