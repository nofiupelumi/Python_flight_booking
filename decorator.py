import functools

# Simulating user roles (you can replace this with your actual authorization logic)
AUTHORIZED_USERS = {"admin", "manager"}

def authorization_decorator(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user in AUTHORIZED_USERS:
            # User is authorized, execute the function
            result = func(user, *args, **kwargs)
            return result
        else:
            # User is not authorized
            print(f"Unauthorized! {user} does not have permission to access this function.")
            # You can raise an exception, return a specific value, or handle it as needed
            return None
    
    return wrapper

# Example usage of the decorator
@authorization_decorator
def sensitive_operation(user):
    print(f"{user} is performing a sensitive operation.")

# Example: Authorized user
authorized_user = "admin"
sensitive_operation(authorized_user)

# Example: Unauthorized user
unauthorized_user = "guest"
sensitive_operation(unauthorized_user)
