from django.contrib import admin

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "nombre", "apellido_paterno", "apellido_materno", "edad", "telefono"]
    search_fields = ["email", "nombre", "apellido_paterno", "apellido_materno", "telefono"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Información Personal", {"fields": ("nombre", "apellido_paterno", "apellido_materno", "edad", "telefono")}),
        ("Permisos", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    ordering = ["email"]