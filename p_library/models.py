from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField() #full_name - будет содержать строковое(str) значение, поэтому используем TextField
    birth_year = models.SmallIntegerField() #birth_year - будет содержать небольшое целочисленное значение(int), поэтому используем SmallIntegerField
    country = models.CharField(max_length=2) #country - это тоже будет строка, но в отличие от full_name у этого атрибута будет ограничение в 2 символа. При сохранении данных автора нам будет необходимо это учитывать. Причина, по которой для отображения страны автора мы выбираем именно CharField, а не TextField в том, что CharField по умолчанию реализует валидацию длины передаваемого значения.
    def __str__(self):
        return self.full_name
    

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=("Автор"), related_name='book_author')
    copy_count = models.PositiveIntegerField(default=1) 
    price = models.DecimalField(max_digits=8, decimal_places=2)
   
    def __str__(self):
        return self.title

class Publisher(models.Model):
    publishing_house = models.TextField()
    books = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.publishing_house