from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    inlines = [ChoiceInline]


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
    list_display = ('poll_name', 'pub_date')
    list_filter = ['pub_date']
    # search_fields = ['question_text']


class QuestionAdmin(admin.StackedInline):
    fieldsets = [
        (None, {'fields': ['question_text', 'type']})]
    inlines =[ChoiceInline]
    list_display = ('question_text')
    model = Question
    extra = 7

# class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_display = ('question_text')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

# admin.site.register(Question, QuestionAdmin)
#
# admin.site.register(Choice)


admin.site.register(Poll, PollAdmin)

admin.site.register(Question)

admin.site.register(Choice)

