from django.contrib import admin

# Register your models here.
from Petstagram1.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'type', 'description']
    sortable_by = ['type', 'age']


admin.site.register(Pet, PetAdmin)