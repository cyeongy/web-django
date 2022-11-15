from django.db import models
from django.urls import reverse


# class Post(models.Model):
#     title = models.CharField('제목', max_length=250)
#     body = models.TextField('내용')
#
#     def __str__(self):
#         return self.title


class Post(models.Model):
    class Meta:
        ordering = ['-id']

    REGION_CHOICE = (
        ('Africa', '아프리카'),
        ('Europe', '유럽'),
        ('Oceania', '오세아니아'),
        ('Asia', '아시아'),
        ('North America', '북아메리카'),
        ('South America', '남아메리카'),
    )

    title = models.CharField('제목', max_length=250)
    body = models.TextField('내용')
    region = models.CharField('지역', max_length=20, choices=REGION_CHOICE, default='Asia')
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author + ":" + self.message


class Tag(models.Model):
    # post = models.ManyToManyField('Post')
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
