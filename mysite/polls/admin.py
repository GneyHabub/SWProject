from django.contrib import admin
from django.contrib import admin
import nested_admin

from .models import Question, Choice, Poll, CustomUser, Group, Student, Teaches, Professor, DoeMember, Votes, Course
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class DoeMemberInline(nested_admin.NestedStackedInline):
    model = DoeMember
    extra = 0
    sortable_options = "id"


class CourseInline(nested_admin.NestedStackedInline):
    model = Course
    extra = 0
    sortable_options = "id"


class StudentAdmin(nested_admin.NestedModelAdmin):
    model = Student
    extra = 0
    sortable_options = "id"


class GroupInline(nested_admin.NestedStackedInline):
    model = Group
    extra = 1
    sortable_options = "id"


class VotesInline(nested_admin.NestedStackedInline):
    model = Votes
    extra = 0
    sortable_options = "id"


class TeachesInline(admin.TabularInline):
    model = Teaches
    extra = 0
    sortable_options = "id"


class ProfessorInline(nested_admin.NestedStackedInline):
    model = Professor
    extra = 0
    sortable_options = "id"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    sortable_options = "id"


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 0
    sortable_option = "id"
    inlines = [ChoiceInline]


class ProfAdmin(UserAdmin):
    list_display = ('email', 'photo', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    list_filter = ('email', 'photo', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'photo', 'password', 'name', 'surname')}),
        ('Permissions', {'fields': ('is_doe', 'is_student', 'is_prof', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'photo', 'password1', 'password2', 'name', 'surname',
                       'is_doe', 'is_student', 'is_prof', 'is_active', 'is_staff')}
         ),
    )
    inlines = [TeachesInline]
    search_fields = ('email',)
    ordering = ('email',)


class DoeAdmin(UserAdmin):
    list_display = ('email', 'photo', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    list_filter = ('email', 'photo', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'photo', 'password', 'name', 'surname')}),
        ('Permissions', {'fields': ('is_doe', 'is_student', 'is_prof', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'photo', 'password1', 'password2', 'name', 'surname',
                       'is_doe', 'is_student', 'is_prof', 'is_active', 'is_staff')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class StudentAdmin(UserAdmin):
    list_display = ('email', 'name', 'surname', 'group', 'graduation_year', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    list_filter = ('email', 'name', 'surname', 'group', 'graduation_year', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'surname', 'group', 'graduation_year')}),
        ('Permissions', {'fields': ('is_doe', 'is_student', 'is_prof', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'surname', 'group', 'graduation_year', 'is_doe',
                       'is_student', 'is_prof', 'is_active', 'is_staff')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class PollAdmin(nested_admin.NestedModelAdmin):
# class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll_name']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Available dates', {'fields': ['open_date', 'close_date']}),
        ('Connection with Prof', {'fields': ['teachers']})
    ]
    inlines = [QuestionInline]
    list_display = ('poll_name', 'pub_date', 'open_date', 'close_date', 'teachers')
    list_filter = ['pub_date']
    sortable_options = "id"
    actions = [Poll.create_similar]



class QuestionAdmin(nested_admin.NestedStackedInline):
    fieldsets = [
        (None, {'fields': ['question_text', 'type']})]
    inlines =[ChoiceInline]
    list_display = ('question_text')
    model = Question
    extra = 7


#     todo maybe it should be changed to Nested User Admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    list_filter = ('email', 'name', 'surname', 'is_doe', 'is_student', 'is_prof', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'surname')}),
        ('Permissions', {'fields': ('is_doe', 'is_student', 'is_prof', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'surname', 'is_doe', 'is_student',
                       'is_prof', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Poll, PollAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Professor, ProfAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Teaches)
admin.site.register(DoeMember, DoeAdmin)
admin.site.register(Votes)
