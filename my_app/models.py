from django.db import models


class Module(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    obj = models.ForeignKey(Module, related_name='reviews')
    email = models.EmailField()
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, default='')
    time_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['obj', 'email', 'comment']

    def __str__(self):
        return ' Review {0.obj} is created at {0.time_creation}, comment: {0.comment}'.format(self)
