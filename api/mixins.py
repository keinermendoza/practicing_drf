from .permissions import CustomDajngoModelPermission
from rest_framework import permissions

class CustomDajngoModelPermissionMixin():
    permission_classes = [CustomDajngoModelPermission, permissions.IsAdminUser]
    # in this case the admin permission is redundant