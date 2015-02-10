from django.contrib import admin
from scripts.models import Script, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ScriptAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'changed_date', 'code']
    fieldsets = [
        (None,               {'fields': ['code']}),
        ('Date information', {'fields': ['pub_date', 'changed_date'], 'classes': ['collapse']}),
    ]
    inlines = [ReviewInline]
    list_display = ('code', 'pub_date', 'changed_date')

admin.site.register(Script, ScriptAdmin)
admin.site.register(Review)
