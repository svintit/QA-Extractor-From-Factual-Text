from django.contrib import admin
from .models import Questions, UniqueSession
from session_handler.models import UserAnswer


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'list_title',
        'inputted_text',
        'qa_list',
        'created',
        'user'
    )


class UniqueSessionAdmin(admin.ModelAdmin):
    list_display = (
        'list_title',
        'inputted_text',
        'qa_list',
        'created',
        'sessionid',
        'user'
    )


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'inputted_text',
        'qalist',
        'created',
        'sessionid'
    )


admin.site.register(Questions, QuestionAdmin)
admin.site.register(UniqueSession, UniqueSessionAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
