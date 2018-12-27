from django.contrib import admin

from cards.models import FlashCardAnswer, FlashCardQuestion, FlashCardCategory


class FlashCardCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Meta:
        model = FlashCardCategory


class FlashCardQuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'created_at', 'content')
    list_filter = ('category', 'author')
    search_fields = ('author__username', 'content')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    class Meta:
        model = FlashCardQuestion


class FlashCardAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at', 'content')
    list_filter = ('question', 'author')
    search_fields = ('author__username', 'content')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    class Meta:
        models = FlashCardAnswer


admin.site.register(FlashCardCategory, FlashCardCategoryAdmin)
admin.site.register(FlashCardQuestion, FlashCardQuestionAdmin)
admin.site.register(FlashCardAnswer, FlashCardAnswerAdmin)
