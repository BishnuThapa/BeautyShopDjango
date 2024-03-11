from django.db import models
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


STATUS_CHOICE = (
    ("process", "Pocessing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered")
)

UNIT = (
    ("kg", "Kilogram"),
    ("pieces", "Pieces")
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published")
)
RATING = (
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐")
)


class Slider(models.Model):
    image = models.ImageField(upload_to='slider',
                              help_text='1920*1280 px')
    heading = models.CharField(max_length=255, null=True, blank=True)
    sub_heading = models.CharField(max_length=255, null=True, blank=True)
    desctiption = RichTextUploadingField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category')
    icon = models.ImageField(upload_to='category')
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category')
    icon = models.ImageField(upload_to='category')
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def sub_category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category')
    icon = models.ImageField(upload_to='category')
    description = RichTextUploadingField(null=True, blank=True)
    ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def brand_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='category')
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, related_name='subcategory')
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, related_name='brand')
    image = models.ImageField(upload_to='products')
    unit = models.CharField(choices=UNIT, max_length=10, default='pieces')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    old_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    description = RichTextUploadingField(null=True, blank=True)
    stock_count = models.CharField(max_length=255, null=True, blank=True)
    life = models.CharField(max_length=255, null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    tags = TaggableManager(blank=True)
    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    exchangeable = models.BooleanField(default=False)
    refundable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = ((self.old_price-self.price)*100)/self.old_price
        return new_price


class ProductImages(models.Model):
    images = models.ImageField(upload_to='productimages')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


# class Cart(models.Model):
#     cart_id = models.CharField(max_length=250, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.cart_id


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     is_active = models.BooleanField(default=True)

#     def sub_total(self):
#         return self.product.price * self.quantity

#     def __str__(self):
#         return self.product


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = RichTextUploadingField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlist'

    def __str__(self):
        return self.product.title
