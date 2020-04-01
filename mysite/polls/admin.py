from django.contrib import admin
from django.contrib import admin
import nested_admin

from .models import Question, Choice, Poll, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    sortable_options = "id"


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 0
    sortable_option = "id"
    inlines = [ChoiceInline]


class PollAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll_name']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Available dates', {'fields': ['open_date', 'close_date']}),
    ]
    inlines = [QuestionInline]
    list_display = ('poll_name', 'pub_date', 'open_date', 'close_date')
    list_filter = ['pub_date']


class QuestionAdmin(nested_admin.NestedStackedInline):
    fieldsets = [
        (None, {'fields': ['question_text', 'type']})]
    inlines =[ChoiceInline]
    list_display = ('question_text')
    model = Question
    extra = 7

# class StudentAdmin(nested_admin.NestedStackedInline):
#     fieldsets = [
#         (None, {'fields': ['question_text', 'type']})]
#     list_display = ('question_text')
#     model = Student
#     extra = 0

# class UserAdmin(nested_admin.NestedModelAdmin):
#     fieldsets = [
#         ('User info', {'fields': ['name', 'email', 'password', 'role']})]
#     list_display = ('name', 'email', 'password', 'role')
#     model = User
#     extra = 0

#     todo maybe it should be changed to Nested User Admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    list_filter = ('email', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_doe', 'is_student', 'is_prof', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_doe', 'is_student', 'is_prof', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

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


# admin.site.register(User, UserAdmin)
admin.site.register(Poll, PollAdmin)

admin.site.register(Question)
admin.site.register(Choice)

