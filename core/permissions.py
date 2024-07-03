from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from core.models import Account


class IsCondo(BasePermission):
    def has_permission(self, request: Request, view):
        user: Account = request.user
        return user.type == Account.Types.CONDO


class IsCondoOrIsCondoStaff(BasePermission):
    def has_permission(self, request: Request, view):
        user: Account = request.user
        return user.type == Account.Types.CONDO or \
            user.type == Account.Types.CONDO_STAFF
