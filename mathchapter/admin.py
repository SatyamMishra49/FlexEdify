from django.contrib import admin
from mathchapter.models import MathChapter
# Register your models here.
class MathChapterAdmin(admin.ModelAdmin):
    list_display = ('mathchapter_title','mathchapter_description')

admin.site.register(MathChapter, MathChapterAdmin)