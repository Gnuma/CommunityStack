from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return "{}".format(self.name)


class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.category.__str__())


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.email, self.username)


class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    time_reading = models.IntegerField()
    link = models.URLField()
    author_name = models.CharField(max_length=255)
    author_img = models.URLField()
    last_updated = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)
