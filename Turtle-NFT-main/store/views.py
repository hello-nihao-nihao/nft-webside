import uuid

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from setting.models import Settings
from store.models import Product, Category, Profile, Post, Sales, Purchase

import os



@login_required(login_url='backstage_login')
def to_order_management(request):
    sales_list = Sales.objects.all()
    buys_list=Purchase.objects.all()
    print(sales_list)
    # email = user.email
    item = []
    item1=[]
    for sales in sales_list:

        item.append({'seller': sales.seller, 'sale_quantity': sales.quantity, 'sales_date':sales.sales_date, 'sales_product_id':sales.product_id})
    for buys in buys_list:
        item1.append({'buyer': buys.buyer, 'buy_quantity': buys.quantity, 'purchase_date': buys.purchase_date, 'buys_product_id': buys.product_id})
    temp = {'sales_item_list': item, 'username': request.user.username,'buys_item_list':item1}
    return render(request,'store/order Management.html',temp)
@login_required(login_url='backstage_login')
def change_User(request):
    if request.method == 'POST':
        user_ = request.POST.get('user')
        username=request.POST.get('username')
        place=request.POST.get('place')
        bio=request.POST.get('bio')
        email=request.POST.get('email')
        money=request.POST.get('money')
        password=request.POST.get('password')
        if Sales.objects.filter(seller=user_).exists():
            sales = Sales.objects.get(seller=user_)
            sales.seller = username
            sales.save()
        if Purchase.objects.filter(buyer=user_).exists():
            buys=Purchase.objects.get(buyer=user_)
            buys.buyer = username
            buys.save()
        user = User.objects.get(username=user_)
        user.set_password(password)
        user.username=username
        user.email=email
        user_profile = Profile.objects.get(user=user)
        user_profile.bio=bio
        user_profile.location=place
        user_profile.money=money
        user.save()
        user_profile.save()
        return redirect('to_User_Management')
@login_required(login_url='backstage_login')
def delete_User(request):
    if request.method == 'POST':

        user_ = request.POST.get('user')

        user = User.objects.get(username=user_)

        user.delete()

        return redirect('to_User_Management')
@login_required(login_url='backstage_login')
def to_User_Management(request):
    user_list=User.objects.all()

    # email = user.email
    item = []
    for user in user_list:
        user_profile = Profile.objects.get(user=user)
        item.append({'email': user.email, 'bio': user_profile.bio, 'profileimg':user_profile.profileimg, 'location':user_profile.location,'money':user_profile.money,'user':user.username})
    temp = {'item_list': item, 'username': request.user.username}
    return  render(request,'store/User Management.html',temp)
@login_required(login_url='backstage_login')
def to_Product_Management(request):
    Post_list = Post.objects.all()
    item = []
    for post in Post_list:
        item.append({'uuid': post.id, 'author': post.author, 'created_at':post.created_at,'image': post.image, 'caption': post.caption,
                     'quantity': int(post.quantity)})
    temp = {'item_list': item, 'username': request.user.username}
    return render(request,'store/Product Management.html',temp)
@login_required(login_url='backstage_login')
def change_Product(request):
    if request.method == 'POST':
        uuid=request.POST.get('uuid')
        post = Post.objects.get(id=uuid)
        caption =request.POST.get('caption')

        author=request.POST.get('author')
        post.caption=caption

        post.author=author
        post.save()
        return redirect('to_Product_Management')
@login_required(login_url='backstage_login')
def delete_Product(request):
    if request.method == 'POST':

        uuid = request.POST.get('uuid')
        print(uuid)
        post = Post.objects.get(id=uuid)
        print(post.author)
        post.delete()

        return redirect('to_Product_Management')
def backstage_login(request):
    return render(request,'store/Backstage_login.html')
#后台用户登录
def backstage_user_login(request):
    if request.method=='POST':
        accont=request.POST['accont']
        password = request.POST['userpassword']

        user = auth.authenticate(username=accont, password=password)
        # 如果用户存在
        if user is not None:
            # messages.info(request, '登录成功')
            # return redirect('signin')
            auth.login(request, user)
            return redirect('backstage_user_detail')
        # 如果用户不存在
        else:
            messages.info(request, '登录失败')
            return redirect('user_login')

def backstage_user_detail(request):
    messages.info(request, "登录成功")
    return redirect('backstage_already_login')


@login_required(login_url='backstage_login')
def backstage_already_login(request):
    Settings.objects.get_or_create(id=1)
    user_object = User.objects.get(username=request.user.username)


    context = {"settings": Settings.objects.first(),'username':user_object.username}

    if context['settings']:
        os.environ['web_name'] = context['settings'].trade_mark
    return render(request, 'backstage_already_login.html', context)

def to_login_html(request):
    return render(request,'store/login_html.html')
# 注册
def signup(request):
    # 如果是post请求
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # 如果密码相等
        if password == password2:
            # 如果邮箱已存在
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('signup')
            # 如果用户名已经存在
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('signup')
            # 如果都不存在
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # 登录
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                # 设置默认的个人信息
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                # 跳转到设置个人信息界面
                return redirect('settings')
        # 如果密码不等，提示
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    # 如果请求不是post，保持在注册界面
    else:
        return render(request, 'store/signup.html')



#个人信息设置
@login_required(login_url='to_login_html')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if not request.FILES.get('image'):
            username=request.user.username
            user_profile.bio = request.POST['bio']
            user_profile.location = request.POST['location']
            user_profile.save()

        if request.FILES.get('image'):
            user_profile.profileimg = request.FILES.get('image')
            user_profile.bio = request.POST['bio']
            user_profile.location = request.POST['location']
            user_profile.save()
        return redirect('main_page_already_login')
    return render(request, 'store/setting.html', {'user_profile': user_profile})
#前往注册页面
def to_sign_up(request):
    return render(request,'store/signup.html')

#用户登录
def user_login(request):
    if request.method=='POST':
        accont=request.POST['accont']
        password = request.POST['userpassword']

        user = auth.authenticate(username=accont, password=password)
        # 如果用户存在
        if user is not None:
            # messages.info(request, '登录成功')
            # return redirect('signin')
            auth.login(request, user)
            return redirect('user_detail')
        # 如果用户不存在
        else:
            messages.info(request, '登录失败')
            return redirect('user_login')
        # 如果不是post请求
    else:
        return render(request, 'store/login_html.html')





def user_detail(request):
    messages.info(request, "登录成功")
    return redirect('main_page_already_login')
# Product Listing






# search query
def search_view(request):
    categories = Category.objects.all()
    results = []
    if request.method == "GET":
        query = request.GET.get("search")
        if query == '':
            query = 'None'
        results = Product.objects.filter(Q(name__icontains=query) | 
        Q(price__icontains=query) | Q(token__icontains=query))
    context = {"query": query, "results": results, "categories": categories}
    return render(request, 'store/search-item.html', context)

def to_mian(request):
    return render(request,'base.html')
def main_page(request):
    Settings.objects.get_or_create(id=1)
    context = {"settings": Settings.objects.first()}

    if context['settings']:
        os.environ['web_name'] = context['settings'].trade_mark
    return render(request, 'base.html', context)

@login_required(login_url='to_login_html')
def main_page_already_login(request):
    Settings.objects.get_or_create(id=1)
    user_object = User.objects.get(username=request.user.username)


    context = {"settings": Settings.objects.first(),'username':user_object.username}

    if context['settings']:
        os.environ['web_name'] = context['settings'].trade_mark
    return render(request, 'base_already_login.html', context)

@login_required(login_url='to_login_html')
def to_user_detail(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    item = []
    user_post=Purchase.objects.filter(buyer=request.user.username)
    for post in user_post:
        if int(post.quantity)<=0:
            continue
        products = Post.objects.filter(id=post.product_id)
        for product in products:
            item.append({'uuid': post.product_id, 'image': product.image, 'quantity': post.quantity, 'caption': product.caption,'author':product.author,'sales_id':post.sales_id})
    temp = {'item_list': item}
    user_item={'bio':user_profile.bio,'profileimg':user_profile.profileimg,'username':request.user.username,
               'location':user_profile.location,'money':user_profile.money,'items':temp}
    return  render(request,'store/show_user.html',user_item)



#退出登录
@login_required(login_url='to_login_html')
def logout(request):
    auth.logout(request)
    return redirect('/')



@login_required(login_url='to_login_html')
def to_upload_html(request):
    username=request.user.username
    temp={'username':username}
    return render(request,'store/upload.html',temp)


#上传
@login_required(login_url='to_login_html')
def upload(request):
    if request.method=='POST':
        author = request.user.username
        id=uuid.uuid4()
        image=request.FILES.get('image')

        caption=request.POST['Trade_name']
        quantity=request.POST['product-quantity']
        price=request.POST['price']
        product = Post(author=author, id=id, image=image,caption=caption,quantity=quantity)
        product.save()
        sales = Sales.objects.create(product=product, seller=request.user.username, quantity=quantity, price=price)
        sales.save()
        messages.info(request,'上传成功')
        return redirect('to_upload_html')
    else:
        return HttpResponse('123')

def marketplace(request):
    Post_list = Post.objects.all()
    item=[]
    for post in Post_list:

        item.append({'uuid':post.id,'author':post.author,'image':post.image,'caption':post.caption,'quantity':int(post.quantity)})
    temp = {'item_list': item,'username':request.user.username}
    return render(request,'store/marketplace.html',temp)

@login_required(login_url='to_login_html')
def buy_someting(request):
    if request.method=='POST':
        price = request.POST.get('price')
        sales_id=request.POST.get('sales_id')
        uuid = request.POST.get('uuid')
        quantity = request.POST.get('quantity')#购买数量
        post=Post.objects.get(id=uuid)
        sales=Sales.objects.get(product=post,sales_id=sales_id)#销售者
        sales.quantity=int(sales.quantity)-int(quantity)
        saller=sales.seller#销售者
        user_object = User.objects.get(username=request.user.username)#购买者
        user_object1 =User.objects.get(username=saller)#被购买者
        user_profile = Profile.objects.get(user=user_object)
        user_profile1 = Profile.objects.get(user=user_object1)
        user_profile.money=user_profile.money-(float(price)*float(quantity))
        user_profile1.money=user_profile1.money+(float(price)*float(quantity))
        post.quantity=int(post.quantity)-int(quantity)
        if Purchase.objects.filter(buyer=request.user.username,product=post).exists():#如果已经购买过
            purchase=Purchase.objects.get(buyer=request.user.username,product=post)
            purchase.quantity=int(purchase.quantity)+int(quantity)
        else:
            purchase = Purchase.objects.create(product=post, buyer=request.user.username, quantity=quantity,sales_id=sales_id)
        sales.save()
        post.save()
        purchase.save()
        user_profile1.save()
        user_profile.save()
        # messages.info(request,"购买成功!")
        return redirect('get_uuid',uuid=uuid)

@login_required(login_url='to_login_html')
def to_Recharge_html(request):
    return render(request,'store/Recharge.html')
#充值
@login_required(login_url='to_login_html')
def Recharge(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        username=request.user.username
        user_object=User.objects.get(username=username)
        user_profile = Profile.objects.get(user=user_object)
        user_profile.money=user_profile.money+float(amount)
        user_profile.save()
    messages.info(request, "充值成功!")
    return redirect('main_page_already_login')

#出售
@login_required(login_url='to_login_html')
def sale(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        price=request.POST.get('price')
        uuid=request.POST.get('uuid')
        sales_id=request.POST.get('sales_id')
        print(price,quantity,uuid,sales_id)
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
        purchase = Purchase.objects.get(buyer=request.user.username,sales_id=sales_id)
        # if int(quantity)>int(purchase.quantity):
        #     messages.info(request, "对不起,出售商品超出数量!")
        #     return redirect('to_user_detail')
        purchase.quantity=int(purchase.quantity)-int(quantity)
        post = Post.objects.get(id=uuid)
        post.quantity=int(post.quantity)+int(quantity)
        post.save()
        if Sales.objects.filter(seller=request.user.username,price=price,product=post).exists():
            sales=Sales.objects.get(seller=request.user.username,price=price,product=post)
            sales.quantity=int(sales.quantity)+int(quantity)
        else:
            sales = Sales.objects.create(product=post, seller=request.user.username, quantity=quantity, price=price)
        sales.save()
        purchase.save()
        user_profile.save()
        # messages.info(request, '出售成功')
        return redirect('to_user_detail')
    else:
        return HttpResponse('123')

@login_required(login_url='to_login_html')
def get_uuid(request,uuid):

    products  = Post.objects.filter(id=uuid)
    item = []
    for  product in products:
        sales = Sales.objects.filter(product=product)
        for sale in sales:
            print(sale.seller,sale.quantity,sale.sales_id,sale.price)
            item.append({'sales_id':sale.sales_id,'uuid': uuid, 'author':product.author,'seller': sale.seller, 'image': product.image, 'caption': product.caption,'quantity': int(sale.quantity),'price':sale.price})




    temp = {'item_list': item,'username':request.user.username}
    return render(request, 'store/marketplace_detail.html', temp)