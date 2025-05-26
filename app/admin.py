from django.contrib import admin
from django.db.models import Count

from app.models import Baker, Cake


# Register your models here.

class BakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return obj and request.user.is_superuser

    def get_queryset(self, request):
        qs = super(BakerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(baker_count=Count('cakes')).filter(baker_count__lt=5)
        return qs


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)

    def has_change_permission(self, request, obj=None):
        return obj and obj.baker.user == request.user

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user=request.user).first()
        cakes = Cake.objects.filter(baker=baker).all()

        if not change and cakes.count() == 10:
            return False

        if Cake.objects.filter(name=obj.name).exists():
            return False

        sum = 0
        for cake in cakes:
            sum += cake.price

        if not change and obj.price + sum > 10000:
            return False

        old_cakes = Cake.objects.filter(id=obj.id).first()

        if change and sum + obj.price - old_cakes.price > 10000:
            return False

        super(CakeAdmin, self).save_model(request, obj, form, change)


admin.site.register(Baker, BakerAdmin)
admin.site.register(Cake, CakeAdmin)
