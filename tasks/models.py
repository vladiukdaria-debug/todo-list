from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tasks:tag-list")


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
    )

    class Meta:
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("tasks:task-list")
