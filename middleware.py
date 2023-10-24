from django.utils import timezone

from user.models import User


class LastActivityTraceMiddleware:
    """
    Set last user's request time
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        member: User = request.user
        if member.is_authenticated:
            member.last_activity = timezone.now()
            member.save()
        return response
