from sentry_sdk import capture_message, capture_exception
from functools import wraps


def log_crud_operation(operation_type):
    """Decorator for CRUD logging operations"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                capture_message(
                    f"{operation_type} operation successful",
                    level="info",
                    extras={
                        "operation": operation_type,
                        "arguments": str(args),
                        "keywords": str(kwargs)
                    }
                )
                return result
            except Exception as e:
                capture_exception(e)
                raise
        return wrapper
    return decorator



def setup_global_error_handler():
    """Sets up a global exception handler"""
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            return

        capture_exception((exc_type, exc_value, exc_traceback))

    import sys
    sys.excepthook = handle_exception
