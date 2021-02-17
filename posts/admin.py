"""Posts admin classes."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    # Custom table view
    list_display = ('pk', 'user', 'title', 'photo')
    list_editable = ('title', 'photo')
    search_fields = (
        'title',
    )
    
    list_filter = (
        'created',
        'modified'
    )

    # Custom edit/create view
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'profile'),)
            
        }),
        ('Posts', {
            'fields': (('title'), ('photo'))
            
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')
