from django.contrib import admin

from cards.models import Category, CardAnswer, CardQuestion, CardSet


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Category


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


class CardSetAdmin(admin.ModelAdmin):
    class Meta:
        model = CardSet


admin.site.register(Category, CategoryAdmin)
admin.site.register(CardQuestion, CardQuestionAdmin)
admin.site.register(CardAnswer, CardAnswerAdmin)
admin.site.register(CardSet, CardSetAdmin)
