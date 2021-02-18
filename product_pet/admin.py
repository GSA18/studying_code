from django.contrib import admin
from .models import ProductPet, Category


@admin.register(ProductPet)
class ProductPetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',
                    'weight', 'created_at', 'get_category')

    def get_category(self, obj):
        list_ = []
        for name_cat in obj.category.all():
            list_.append(name_cat.name)
        return list_


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
