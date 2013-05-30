#ABOUT CUSTOM DECORATOR
Custom decorator for multiple permissions, which will check for all permissions and allow user if he passes test. 
    Ex -      
        @permission_set_required(perm=['app.add_app', 'app.change_app'], perm_check='AND')
            1- perm_check is the factor through which user permission is being checked like if perm_check = AND then user must have all permission listed in perm
            2- if perm_check=OR then if user has any one of them can pass the test and will be able to access the url.
            3 - perm_check is restricted for AND and OR, if any of them not found, will raise NotValidCheck exception. 

#User manual
  1- download application.
  2- Add it to your repo
  3- import from custom_decorator.custom_decorator import permission_set_required
  4- and use it  EX  - 
     1 - simple views
           @permission_set_required(perm=['app.add_app', 'app.change_app'], perm   _check='AND')
           def view(request):
               pass

            -----OR----
     2 - Class based Views
            
            class MyView(View):
                @method_decorator(permission_set_required(perm=['app.add_app', 'app.change_app'], p   erm   _check='AND'))
                def get(request):
                    pass
            

#Dependency 
    1- django > = 1.3





