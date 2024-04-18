from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, staff_required
from .models import Idea, UserProfile, PostAwareness, PostOthers, Reporting, PostEmergency, PostRecommendations, PostInnovation, PostSuggestions, PostComplain
from django.utils.html import escape
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Generate OTP token
            token_generator = default_token_generator
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            # Construct verification URL
            current_site = get_current_site(request)
            verification_url = f"http://{current_site.domain}/verify/{uid}/{token}/"

            # Compose email subject and content
            subject = 'Verify Your Account'
            message = render_to_string('verify_account_email.html', {
                'user': user,
                'verification_url': verification_url,
            })

            # Send email
            send_mail(
                subject,
                message,
                user.email,  # Use user's email address as sender
                [user.email],  # User's email address
                fail_silently=False,
            )

            # Create a UserProfile instance and link it to the user
            UserProfile.objects.create(user=user, role='regular_user')

            auth_login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    
    # Additional context data
    context = {
        'title': 'Register - Virtual Idea Hub',
        'message': 'Please register to continue.',
        'form': form  # Pass the form to the template
    }
    return render(request, 'register.html', context)


def home_view(request):
    # Add any necessary logic here
    return render(request, 'home.html')

@login_required
def user_dashboard(request):
    # Get the current user's information
    user = request.user

    # Get the user's submitted ideas
    submitted_ideas = Idea.objects.filter(user=user)

    context = {
        'user': user,
        'submitted_ideas': submitted_ideas
    }

    return render(request, 'user_dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def search_results(request):
    query = request.GET.get('query')
    results = Idea.objects.filter(title__icontains=query)
    context = {'results': results, 'query': query}  # Include the query in the context
    return render(request, 'search_results.html', context)

# Define other views...
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def about(request):
    # Your view logic here
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    # Your view logic here
    return render(request, 'dashboard.html') 

def profile(request):
    # Your view logic here
    return render(request, 'profile.html')

def profile_settings_submit(request):
    # Your view logic here
    # This function should handle form submission or any other processing related to profile settings
    return render(request, 'profile_settings_submit.html')

def contact_form_submit(request):
    # Your view logic here
    # This function should handle form submission or any other processing related to the contact form
    return render(request, 'contact_form_submit.html')  # Assuming you have a 'contact_form_submit.html' template

@login_required
def home(request):
    return render(request, 'base.html')

@login_required
@admin_required
def admin_dashboard(request):
    # View logic for admin dashboard
    return render(request, 'admin_dashboard.html')

@login_required
@staff_required
def staff_dashboard(request):
    # View logic for staff dashboard
    return render(request, 'staff_dashboard.html')

def idea_list(request):
    ideas = Idea.objects.all()
    context = {'ideas': ideas}
    return render(request, 'myapp/idea_list.html', context)

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    context = {'idea': idea}
    return render(request, 'myapp/idea_detail.html', context)

def send_category_email(category_model, request, template_name, subject_template_name, email_field):
    if request.method == 'POST':
        # Handle form submission
        # Assuming you have form data in request.POST

        # Save the submitted post for the category
        new_post = category_model.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            # Set other fields as needed
        )

        # Retrieve the email of the category manager
        category_manager_email = getattr(new_post, email_field)  # Get email from model instance

        # Compose email subject and content
        subject = render_to_string(subject_template_name, {'post': new_post})
        subject = ''.join(subject.splitlines())  # Remove line breaks
        context = {'post': new_post}  # You can pass additional context as needed
        email_content = render_to_string(template_name, context)

        # Send email to category manager
        send_mail(
            subject,
            email_content,
            'sender@example.com',  # Your sender email address
            [category_manager_email],  # Category manager email
            html_message=email_content,  # HTML content
        )

        # Handle success or redirect to a thank you page
    else:
        # Render form for category post submission
        pass
    return render(request, template_name)

def post_awareness(request):
    return send_category_email(PostAwareness, request, 'post_awareness.html', 'email/post_awareness_notification_subject.txt', 'manager_email')

def post_others(request):
    return send_category_email(PostOthers, request, 'post_others.html', 'email/post_others_notification_subject.txt', 'manager_email')

def post_reporting(request):
    if request.method == 'POST':
        # Create a Reporting instance with form data
        new_reporting = Reporting(
            report_name=request.POST.get('report_name'),
            location=request.POST.get('location'),
            report_description=request.POST.get('report_description'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            registration_number=request.POST.get('registration_number'),
            department=request.POST.get('department'),
            school=request.POST.get('school'),
            telephone=request.POST.get('telephone'),
            email=request.POST.get('email'),
            # Add this line to get the 'title' field
        )
        new_reporting.save()
        # Add any additional logic or redirect to a success page
        return HttpResponse("Reporting submitted successfully!")  # Return a success response
    else:
        # Render form for GET request
        return render(request, 'post_reporting.html')

def post_emergency(request):
    return send_category_email(PostEmergency, request, 'post_emergency.html', 'email/post_emergency_notification_subject.txt', 'manager_email')

def post_recommendations(request):
    return send_category_email(PostRecommendations, request, 'post_recommendations.html', 'email/post_recommendations_notification_subject.txt', 'manager_email')

def post_innovation(request):
    return send_category_email(PostInnovation, request, 'post_innovation.html', 'email/post_innovation_notification_subject.txt', 'manager_email')

def post_suggestions(request):
    return send_category_email(PostSuggestions, request, 'post_suggestions.html', 'email/post_suggestions_notification_subject.txt', 'manager_email')

def post_complain(request):
    return send_category_email(PostComplain, request, 'post_complain.html', 'email/post_complain_notification_subject.txt', 'manager_email')


@login_required
def user_dashboard(request):
    # Get the current user's information
    user = request.user

    # Get the user's profile information
    user_profile = UserProfile.objects.get(user=user)

    # Check if the user has submitted any reports
    submitted_reports = Reporting.objects.filter(email=user.email)

    context = {
        'user': user,
        'user_profile': user_profile,
        'submitted_reports': submitted_reports
    }

    return render(request, 'user_dashboard.html', context)

from .models import Reporting

from .models import Reporting

def reporting_dashboard(request):
    # Retrieve all reports from the Reporting model
    reports = Reporting.objects.all()

    # Pass the reports to the template context
    context = {
        'reports': reports
    }

    # Render the dashboard template with the reports data
    return render(request, 'dashboard.html', context)
