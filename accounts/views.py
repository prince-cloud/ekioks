from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            user.set_password(data['password'])
            user.save()
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})

@login_required
def dashboard(request):
    user = request.user
    productlist = user.product_set.all()
    paginator = Paginator(productlist, 10)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    return render(request, 'registration/dashboard.html', {'user':request.user, 'products': productlist})



def logoutview(request):
    logout(request)
    return redirect('products:product_list')

def password_change_done(request):
    return redirect('accounts:password_change_done')


def editprofile(request):
    return redirect('accounts:editprofile')

