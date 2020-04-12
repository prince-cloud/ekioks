from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Count
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from .forms import Sellform
# Create your views here.


def productlist(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_product=Count('product'))
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(title__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query) 
        )

    paginator = Paginator(productlist, 10)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    template = 'product/product_list.html'

    context = {'product_list':productlist, 'category_list':categorylist, 'category':category }
    return render(request,  template, context)


def productdetail(request, product_slug):
    print(product_slug)
    productdetail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'product/product_detail.html'
    context = {'product_detail':productdetail,'product_images' : productimages}
    return render(request, template, context)    

@login_required
def postad(request):
    if request.method == 'POST':
        form = Sellform(data=request.POST, files=request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.owner = request.user
            newproduct.save()
            return redirect('accounts:dashboard')
    else:
        form = Sellform()
    return render(request, 'product/postad.html',{'form':form})



@login_required
def edititemview(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.user != product.owner:
        return Http404()
    if request.method == 'POST':
        form = Sellform(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.owner = request.user
            newproduct.save()
            return redirect('accounts:dashboard')
    else:
        form = Sellform(instance=product)
    return render(request, 'product/postad.html',{'form':form})
