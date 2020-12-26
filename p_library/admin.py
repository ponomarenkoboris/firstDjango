from django.contrib import admin
from p_library.models import Book, Author, Publisher
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name', 'price')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    @staticmethod
    def book_title(obj):
        return obj.books.title
    list_display = ('publishing_house', 'book_title')
    fields = ('publishing_house', 'books')

#Фильтр по издательствам
class ExpiryDateFilter(SimpleListFilter):

    title = _('Publishers')

    parameter_name = 'publishing_house'

    def lookups(self, request, model_admin):
        """
            List of values to allow admin to select
        """
        return (
            ('valid', _('All Valid')),
            ('invalid', _('All Invalid')),
        )

    def queryset(self, request, queryset):
        """
            Return the filtered queryset
        """

        if self.value() == 'valid':
            return queryset.filter(publishing_house=Publisher.objects.all())
        elif self.value() == 'invalid':
            return queryset.filter(Publisher.exclude(Publisher.objects.all()))
        else:
            return queryset

# Фильр в админке для юзеров. 
class PersonAdmin(admin.ModelAdmin):
    list_filter = (ExpiryDateFilter,)