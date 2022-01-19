from django.contrib import admin

from .models import Article, Tag, TagsArticles

from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class TagsArticlesInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            main = form.cleaned_data['is_main']
            if main == True:
                count += 1

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if count == 0:
            raise ValidationError('Выберите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class TagsArticlesInline(admin.TabularInline):
    model = TagsArticles
    formset = TagsArticlesInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [TagsArticlesInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
