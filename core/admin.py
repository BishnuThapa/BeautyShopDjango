from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading', 'updated_at')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'ordering', 'created_at', 'updated_at')
    list_editable = ('ordering',)



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Wishlist)
