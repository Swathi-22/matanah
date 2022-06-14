from django.contrib import admin
from .models import Category,Product,Gallery,Contact




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'firstname',)
