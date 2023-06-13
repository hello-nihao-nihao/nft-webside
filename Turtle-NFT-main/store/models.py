import uuid
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(default='default.png', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    token = models.CharField(max_length=100, null=True, blank=True, default="TTC")
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    block_hash = models.CharField(max_length=1000, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transaction')
    discord_link = models.CharField(max_length=500, null=True)
    wallet_address = models.CharField(max_length=10000, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_on',)
    
    def __str__(self):
        return f"Discord Buyer {self.discord_link} purchased {self.product.id}"
    
    def product_id(self):
        return self.product.id
    
    def transaction_id(self):
        return f" Transaction {self.id}"



User = get_user_model()
class Profile(models.Model):
    # 当前操作的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 个人介绍
    bio = models.TextField(blank=True)
    # 头像
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    # 地域
    location = models.CharField(max_length=100, blank=True)
    #用户余额
    money = models.FloatField(max_length=100,default=0.00)

    class Meta:
        db_table='Profile'
# 上传的nft作品
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,max_length=100)
    # 作者
    author = models.CharField(max_length=100)
    # 发的nft图片
    image = models.ImageField(upload_to='post_images')
    # 标题,也就是商品的名称
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    quantity = models.IntegerField(default=1) # 剩余数量
    class Meta:
        db_table='Post'



class Purchase(models.Model):
    # 购买表
    purchase_id = models.AutoField(primary_key=True) # 购买ID
    product = models.ForeignKey(Post, on_delete=models.CASCADE) # 商品外键
    buyer = models.CharField(max_length=100)  # 购买者ID
    quantity = models.IntegerField() # 购买数量
    purchase_date = models.DateTimeField(auto_now_add=True) # 购买时间
    sales_id=models.IntegerField()

class Sales(models.Model):
    # 销售表
    sales_id = models.AutoField(primary_key=True) # 销售ID
    product = models.ForeignKey(Post, on_delete=models.CASCADE) # 商品外键
    seller= models.CharField(max_length=100) # 销售者
    quantity = models.IntegerField() # 销售数量
    price = models.DecimalField(max_digits=8, decimal_places=2) # 销售价格
    sales_date = models.DateTimeField(auto_now_add=True) # 销售时间









