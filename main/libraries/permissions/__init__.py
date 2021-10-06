from rest_framework import permissions


class HasPaidPlan(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.has_paid_plan()

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.has_paid_plan()


class HasPaidPlanOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS or request.user.has_paid_plan()

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS or request.user.has_paid_plan()


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_client()

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_client()


class IsConsultantAndReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS and request.user.is_consultant()

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS and request.user.is_consultant()


class IsSupplierAndReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS and request.user.is_supplier()

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS and request.user.is_supplier()


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if user is owner of given object.
        """
        return request.method in permissions.SAFE_METHODS or request.user == obj.owner

