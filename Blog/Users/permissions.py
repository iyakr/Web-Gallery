from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


# class AdminsPermissions(BasePermission):
#     # allowed_user_roles = (User.Superuser)
#
#     def has_permission(self, request, view):
#         is_allowed_user = request.user.role in self.allowed_user_roles
#         return is_allowed_user