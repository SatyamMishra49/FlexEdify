from django.contrib import admin
from chapter.models import Chapter
# Register your models here.

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_title', 'chapter_description')

admin.site.register(Chapter,ChapterAdmin)