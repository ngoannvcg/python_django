from django.contrib import admin
# Register your models here.
from django.contrib.admin.utils import flatten_fieldsets

from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date']}), ]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInLine]


admin.site.register(Question
                    # , QuestionAdmin
                    )
# admin.site.register(Choice)
