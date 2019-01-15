from django.contrib import admin

from card.models import CardAnswer, CardQuestion, CardCategory


class CardCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Meta:
        model = CardCategory


class CardQuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'created_at', 'content')
    list_filter = ('category', 'author')
    search_fields = ('author__username', 'content')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    class Meta:
        model = CardQuestion


class CardAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at', 'content')
    list_filter = ('question', 'author')
    search_fields = ('author__username', 'content')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    class Meta:
        models = CardAnswer


admin.site.register(CardCategory, CardCategoryAdmin)
admin.site.register(CardQuestion, CardQuestionAdmin)
admin.site.register(CardAnswer, CardAnswerAdmin)
