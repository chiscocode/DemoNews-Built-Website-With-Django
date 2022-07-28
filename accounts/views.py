from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


# Create your views here.

def home(request):
    mainpost=MainPost.objects.filter(status=1).order_by('-date_added')
    featuredpost=FeaturedPost.objects.filter(status=1).order_by('-date_added')
    posts=Post.objects.filter(status=1).order_by('-date_added')
    politics=Post.objects.filter(category__title__in=["Politics"])
    sports=Post.objects.filter(category__title__in=["Sports"])
    businesss=Post.objects.filter(category__title__in=["Business"])
    entertainments=Post.objects.filter(category__title__in=["Entertainment"])
    advertone = AdvertisementOne.objects.all()
    advertthree = AdvertisementThree.objects.all()
    popular =Post.objects.annotate(total_views=Count('viewers')).filter(total_views__gt=0).order_by('-total_views')

    #pagination
    popularpaginator = Paginator(popular, 4)
    popularpage = request.GET.get('page')
    popularusers = popularpaginator.get_page(popularpage)

    #pagination
    advertonepaginator = Paginator(advertone, 1)
    advertonepage = request.GET.get('page')
    advertoneusers = advertonepaginator.get_page(advertonepage)

    

    #pagination
    advertthreepaginator = Paginator(advertthree, 1)
    advertthreepage = request.GET.get('page')
    advertthreeusers = advertthreepaginator.get_page(advertthreepage)


    #pagination
    entertainmentspaginator = Paginator(entertainments, 3)
    entertainmentspage = request.GET.get('page')
    entertainmentsusers = entertainmentspaginator.get_page(entertainmentspage)


    #pagination
    businessspaginator = Paginator(businesss, 3)
    businessspage = request.GET.get('page')
    businesssusers = businessspaginator.get_page(businessspage)


    #pagination
    sportspaginator = Paginator(sports, 3)
    sportspage = request.GET.get('page')
    sportsusers = sportspaginator.get_page(sportspage)

    #pagination
    politicspaginator = Paginator(politics, 3)
    politicspage = request.GET.get('page')
    politicsusers = politicspaginator.get_page(politicspage)

    #pagination
    mainpaginator = Paginator(mainpost, 1)
    mainpage = request.GET.get('page')
    mainusers = mainpaginator.get_page(mainpage)

    #pagination
    featuredpaginator = Paginator(featuredpost, 2)
    featuredpage = request.GET.get('page')
    featuredusers = featuredpaginator.get_page(featuredpage)

    
    #pagination
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    newsletterfor = NewsletterForm()
    if request.method == 'POST':
        newsletterfor = NewsletterForm(request.POST,request.FILES)
        if newsletterfor.is_valid():
            newsletterfor.save()
        return render(request,'emailsent.html')

    context={'mainpost':mainusers, 'featuredpost': featuredusers,'posts':users,'newsletterfor':newsletterfor,'politics':politicsusers,'sports':sportsusers,'businesss':businesss,'entertainments':entertainmentsusers,'advertonepaginator':advertoneusers,'advertthreepaginator':advertthreeusers,'popular':popularusers}
        
    return render(request,'index.html',context)

def category (request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    advertone = AdvertisementOne.objects.all()
    advertthree = AdvertisementThree.objects.all()

    #pagination
    advertonepaginator = Paginator(advertone, 1)
    advertonepage = request.GET.get('page')
    advertoneusers = advertonepaginator.get_page(advertonepage)

    

    #pagination
    advertthreepaginator = Paginator(advertthree, 1)
    advertthreepage = request.GET.get('page')
    advertthreeusers = advertthreepaginator.get_page(advertthreepage)


    newsletterfor = NewsletterForm()
    if request.method == 'POST':
        newsletterfor = NewsletterForm(request.POST,request.FILES)
        if newsletterfor.is_valid():
            newsletterfor.save()
        return render(request,'emailsent.html')



    context={'category':category,'newsletterfor':newsletterfor,'advertonepaginator':advertoneusers,'advertthreepaginator':advertthreeusers}
    return render(request,'category.html',context)


def MainPostdetail(request,slug):
    post=MainPost.objects.get(slug=slug)
    comments= post.maincomments.all()
    categorys=Category.objects.all()
    advertone = AdvertisementOne.objects.all()
    advertthree = AdvertisementThree.objects.all()

    #pagination
    advertonepaginator = Paginator(advertone, 1)
    advertonepage = request.GET.get('page')
    advertoneusers = advertonepaginator.get_page(advertonepage)

    

    #pagination
    advertthreepaginator = Paginator(advertthree, 1)
    advertthreepage = request.GET.get('page')
    advertthreeusers = advertthreepaginator.get_page(advertthreepage)

    new_comment= None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('mainpostdetails',args = [str(post.slug)]))
    else:
        form = CommentForm()

    similar_posts=list(post.category.posts.exclude(id=post.id))

    if len(similar_posts) >= 4:
        similar_posts = random.sample(similar_posts, 3)
    
    newsletterfor = NewsletterForm()
    if request.method == 'POST':
        newsletterfor = NewsletterForm(request.POST,request.FILES)
        if newsletterfor.is_valid():
            newsletterfor.save()
        return render(request,'emailsent.html')


    context={'post':post,'form':form,'new_comment' : new_comment,'similar_posts': similar_posts,'comments':comments,'categorys':categorys,'newsletterfor':newsletterfor,'advertonepaginator':advertoneusers,'advertthreepaginator':advertthreeusers}
    return render(request, 'postdetails.html',context)

def PostDetail(request,slug):
    post=Post.objects.get(slug=slug)
    commenting= post.commen.all()
    categorys=Category.objects.all()
    advertone = AdvertisementOne.objects.all()
    advertthree = AdvertisementThree.objects.all()

    #pagination
    advertonepaginator = Paginator(advertone, 1)
    advertonepage = request.GET.get('page')
    advertoneusers = advertonepaginator.get_page(advertonepage)

    

    #pagination
    advertthreepaginator = Paginator(advertthree, 1)
    advertthreepage = request.GET.get('page')
    advertthreeusers = advertthreepaginator.get_page(advertthreepage)

    new_comment= None
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('postdetails',args = [str(post.slug)]))
    else:
        form = PostCommentForm()
        

    similar_posts=list(post.category.posts.exclude(id=post.id))

    if len(similar_posts) >= 4:
        similar_posts = random.sample(similar_posts, 3)
    
    newsletterfor = NewsletterForm()
    if request.method == 'POST':
        newsletterfor = NewsletterForm(request.POST,request.FILES)
        if newsletterfor.is_valid():
            newsletterfor.save()
        return render(request,'emailsent.html')


    context={'post':post,'form':form,'new_comment':new_comment,'similar_posts': similar_posts,'commenting':commenting,'categorys':categorys,'newsletterfor':newsletterfor,'advertonepaginator':advertoneusers,'advertthreepaginator':advertthreeusers}
    return render(request, 'details.html',context)


def FeaturedDetail(request,slug):
    post=FeaturedPost.objects.get(slug=slug)
    comments= post.featuredcomments.all()
    categorys=Category.objects.all()
    advertone = AdvertisementOne.objects.all()
    advertthree = AdvertisementThree.objects.all()

    #pagination
    advertonepaginator = Paginator(advertone, 1)
    advertonepage = request.GET.get('page')
    advertoneusers = advertonepaginator.get_page(advertonepage)

    

    #pagination
    advertthreepaginator = Paginator(advertthree, 1)
    advertthreepage = request.GET.get('page')
    advertthreeusers = advertthreepaginator.get_page(advertthreepage)

    new_comment= None
    if request.method == 'POST':
        form = FeaturedCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('featureddetails',args = [str(post.slug)]))
    else:
        form = FeaturedCommentForm()

    similar_posts=list(post.category.posts.exclude(id=post.id))

    if len(similar_posts) >= 4:
        similar_posts = random.sample(similar_posts, 3)
    
    newsletterfor = NewsletterForm()
    if request.method == 'POST':
        newsletterfor = NewsletterForm(request.POST,request.FILES)
        if newsletterfor.is_valid():
            newsletterfor.save()
        return render(request,'emailsent.html')


    context={'post':post,'form':form,'new_comment' : new_comment,'similar_posts': similar_posts,'comments':comments,'categorys':categorys,'newsletterfor':newsletterfor,'advertonepaginator':advertoneusers,'advertthreepaginator':advertthreeusers}
    return render(request,'featured.html',context)


def ContactUs(request):
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST,request.FILES)
        if contact.is_valid():
            contact.save()
            return render(request,'sent.html')

    return render(request,'contact.html')

def AboutUs(request):
    return render(request,'about.html')