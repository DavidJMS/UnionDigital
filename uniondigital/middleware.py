# from Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletationMiddleware:
    """
        Middlewaree to ensure that each user profile has the image, 
        position and biography fields filled in
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        # Get response
        response = self.get_response(request)
        if request.path not in [reverse('accounts:update_profile')]:
            if not request.user.is_anonymous:
                if not request.user.is_staff:
                    profile = request.user.profile
                    if not profile.position or not profile.biography or not profile.picture:
                        return redirect('accounts:update_profile')
        return response
