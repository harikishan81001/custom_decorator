#ABOUT CUSTOM DECORATOR

    Custom decorator for multiple permissions, which will check for all permissions and allow user if he passes test.

    
#Allowed Operations 

    ALLOWED_CHECK = ['AND', 'OR', 'NOT']
    1- AND - check for all, user must have all those permissions
    2- OR - Passes if user has any of thease permissions 
    3- NOT - if user has any of mentioned permissions, access will be restricted. 

#User manual
  
  1- download application.
  
  2- Add it to your repo
  
  3- import from custom_decorator.custom_decorator import permission_set_required
  
  4- and use it  
  EX - 
  
     1 - simple views
     
        @permission_set_required(perm=['app.add_app', 'app.change_app'], perm_check='AND')
        def view(request):
            pass
               
     2 - Class based Views
            
        class MyView(View):
            @method_decorator(permission_set_required(perm=['app.add_app', 'app.change_app'], perm_check='AND'))
            def get(request):
                pass
            

#Dependency 
    1- django > = 1.3





