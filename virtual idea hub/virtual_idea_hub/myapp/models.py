from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('staff', 'Staff'), ('regular_user', 'Regular User')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.date}"

class EmailQueue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.user.username} on {self.sent_date}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    manager_email = models.EmailField(default="example@example.com")  # Provide a default value

    def __str__(self):
        return self.name

class PostAwareness(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostOthers(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Reporting(models.Model):
    report_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    report_description = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.report_name


class PostEmergency(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostRecommendations(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostInnovation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostSuggestions(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostComplain(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title