from django.contrib import admin

from .models import Home,About,Profile,Category,Skills,Portfolio,Message

admin.site.register(Home)
class profileInline(admin.TabularInline):
    model=Profile
    extra=1
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[profileInline]
    
class SkillsInline(admin.TabularInline):
    model=Skills
    extra=2
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines=[SkillsInline]
    
admin.site.register(Portfolio)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'created_at')
    search_fields = ('name', 'phone', 'address')