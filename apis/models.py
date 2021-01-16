from django.db import models
from django.core.validators import FileExtensionValidator



# Create your models here

class Branch(models.Model):
    branch_text = models.CharField(max_length=30)

    def __str__(self):
        return self.branch_text

class Category(models.Model):
    branch_text = models.ForeignKey(Branch, on_delete = models.CASCADE)
    category_text = models.CharField(max_length=30)
    category_image = models.ImageField(upload_to = 'media/',null = False)

    def __str__(self):
        return self.category_text

    def delete(self,*args,**kwargs):
        self.category_image.delete()
        super().delete(*args,**kwargs)

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField(primary_key=True, max_length=200)
    contact_number = models.IntegerField(unique=True, default=0)
    roll_no = models.CharField(max_length=200)
    user_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.user_mail

    def delete(self,*args,**kwargs):
        self.user_image.delete()
        super().delete(*args,**kwargs)


class Book(models.Model):
    book_name = models.CharField(max_length=100, blank=False, null=False)
    book_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    book_serial_id = models.IntegerField(primary_key=True, blank=False, null=False)
    book_description = models.CharField(max_length=1000, blank=True, null=True)
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_by')
    bought_by = models.ManyToManyField(User, related_name='bought_by',blank = True)
    book_image = models.ImageField(upload_to='media/', null=False)
    book_pdf = models.FileField(upload_to = 'media/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null = False,)
    publish_date = models.DateTimeField(auto_now_add=True)
    review_stars_count = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    publication = models.CharField(max_length=200)
    price = models.FloatField(null=False, blank=False)
    no_of_pages = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.book_name

    def delete(self,*args,**kwargs):
        self.book_image.delete()
        self.book_pdf.delete()
        super().delete(*args,**kwargs)


class Payment(models.Model):
    transaction_id = models.CharField(primary_key=True, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)
    transaction_amount = models.FloatField()
    def __str__(self):

        return self.transaction_id
