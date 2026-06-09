from django.db import models


class Blog(models.Model):
    """
    Blog model
    """

    title = models.CharField(max_length=255, help_text='Required. Max length 255 chars.')
    article = models.TextField()
    date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', 'title']


class BlogImage(models.Model):
    """
    Blog images (a space to upload images, which can be linked to in a blog)
    """

    image = models.ImageField(upload_to='blog', default='default.jpg')
    image_description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return f"Image: {self.image_description}"
