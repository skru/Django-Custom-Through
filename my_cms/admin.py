from django.contrib import admin
from my_cms.models import *

admin.site.register(Industry)
admin.site.register(Location)
admin.site.register(Age)
admin.site.register(Gender)
admin.site.register(Income)
admin.site.register(Relationship)
admin.site.register(Children)


class WebsiteInlineAdmin(admin.TabularInline):
    model = Through
    extra = 0
    #readonly_fields = ['website','crawl']
    readonly_fields = ['crawl']
    fields = ['website', 'crawl', 'industry', 'location',
              'age', 'gender', 'income', 'relationship',
              'children']


class CrawlAdmin(admin.ModelAdmin):
    inlines = [WebsiteInlineAdmin, ]
    list_display = ('created_at',)
    readonly_fields = ['created_at']
    list_filter = ['created_at']
    fieldsets = (
        (None, {
            "fields": ('created_at',)
        }),
    )


admin.site.register(Crawl, CrawlAdmin)


class WebsiteAdmin(admin.ModelAdmin):
    inlines = [WebsiteInlineAdmin, ]

admin.site.register(Website, WebsiteAdmin)
