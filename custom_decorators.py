__author__ = 'hari'

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from exceptions import Exception


class NotValidCheck(Exception):
    pass

ALLOWED_CHECK = ['OR', 'AND']

def permission_set_required(
        perm, perm_check='OR',
        login_url=None, raise_exception=False ):
    """
    decorator for the views that check whether a user has
    a particular set of permissions based on perm_check like
     1 - if perm_check == 'OR'
         User must have a single permission from the set of permission
     2 - if perm_check == 'AND'
        User must have all permissions from the set to pass decorator
    if raise_exception is given then PermissionDenied exception will be
      raised.
    """

    def check_perms(user):
        if perm_check not in ALLOWED_CHECK:
            raise NotValidCheck(
                'perm_check is not valid expected is "AND", '
                ' "OR" but found %s' % perm_check)
        if not isinstance(perm, list):
            return permission_required(
                perm, login_url=login_url,
                raise_exception=raise_exception)
        else:
            if perm_check=='OR':
                return check_or_perms(user, perm)
            elif perm_check=='AND':
                return check_and_perms(user, perm)

    def check_or_perms(user, perm_list):
        flag = False
        for each in perm_list:
            if user.has_perm(each):
                flag = True

        #In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        return flag


    def check_and_perms(user, perm_list):
        flag = False
        for each in perm_list:
            if user.has_perm(each):
                flag = True
            else:
                flag = False

        #In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        return flag

    return user_passes_test(check_perms, login_url = login_url)


