from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status')
    ordering = ('-published','title')
    list_filter = ('status','published')
    search_fields = ('title','description')
    row_id_fields = ('author')
    date_hierarchy = 'published'
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    list_display_links = ('title','published')


