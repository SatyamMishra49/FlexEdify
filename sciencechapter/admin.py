from django.contrib import admin
from sciencechapter.models import ScienceChapter
# Register your models here.
class ScienceChapterAdmin(admin.ModelAdmin):
    list_display = ('sciencechapter_title','sciencechapter_description')

admin.site.register(ScienceChapter, ScienceChapterAdmin)