from django.contrib import admin

from .models import PackageTheme, PackageType, Destination

@admin.register(PackageTheme)
class PackageThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass
