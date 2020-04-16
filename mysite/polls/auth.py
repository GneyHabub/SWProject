from django.contrib.auth.backends import ModelBackend
from .models import CustomUser, Professor, Student, DoeMember


class AuthBackend(ModelBackend):
    """
    Backend using ModelBackend, but attempts to "downcast"
    the user into a PersonUser or KitUser.
    """

    def authenticate(self, *args, **kwargs):
        return self.downcast_user_type(super().authenticate(*args, **kwargs))

    def get_user(self, *args, **kwargs):
        return self.downcast_user_type(super().get_user(*args, **kwargs))

    def downcast_user_type(self, user):
        try:
            kit_user = Student.objects.get(pk=user.pk)
            return kit_user
        except:
            pass

        try:
            person_user = DoeMember.objects.get(pk=user.pk)
            return person_user
        except:
            pass

        try:
            person_user = Professor.objects.get(pk=user.pk)
            return person_user
        except:
            pass

        try:
            person_user = CustomUser.objects.get(pk=user.pk)
            return person_user
        except:
            pass

        return user
