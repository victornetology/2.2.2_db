from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope
from django.contrib import admin

class TagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data and form.cleaned_data['is_main']:
                main_count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        if main_count != 1:
            raise ValidationError('Основной тег должден быть ровно один!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagsInline(admin.TabularInline):
    model = Scope
    formset = TagsInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInline]
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
