from django.contrib import admin

# Register your models here.

@admin.register(Tarea)
# Register your models here.
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','severity')
    search_fields = ('id', 'severity')



admin.site.register()