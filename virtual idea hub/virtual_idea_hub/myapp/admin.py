from django.contrib import admin
from .models import UserProfile, Idea, Question, Feedback, EmailQueue, Category
from .models import PostAwareness, PostOthers, Reporting, PostEmergency, PostRecommendations, PostInnovation, PostSuggestions, PostComplain


# Define admin classes for each model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'creation_date', 'status', 'category')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'creation_date', 'status', 'category')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'idea', 'question', 'date')
    list_filter = ('idea', 'question')

class EmailQueueAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'sent_date')
    search_fields = ('subject', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'creation_date')
    search_fields = ('name', 'description', 'manager_email')  # Include 'manager_email' in search fields

# Register your models

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(EmailQueue, EmailQueueAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostAwareness)
admin.site.register(PostOthers)
admin.site.register(Reporting)
admin.site.register(PostEmergency)
admin.site.register(PostRecommendations)
admin.site.register(PostInnovation)
admin.site.register(PostSuggestions)
admin.site.register(PostComplain)

