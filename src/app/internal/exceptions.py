from rest_framework.views import exception_handler


def core_exception_handler(exception, context):
    response = exception_handler(exception, context)
    handlers = {"ValidationError": _handle_generic_error}

    exception_class = exception.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exception, context, response)

    return response


def _handle_generic_error(exception, context, response):
    response.data = {"errors": response.data}

    return response
