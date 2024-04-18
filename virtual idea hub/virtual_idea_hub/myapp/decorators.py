from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def admin_required(view_func):
    """
    Decorator that checks if the user is an admin.
    """
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.userprofile.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not admin
    return _wrapped_view

def staff_required(view_func):
    """
    Decorator that checks if the user is a staff member.
    """
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.userprofile.role == 'staff':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not staff
    return _wrapped_view
