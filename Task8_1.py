def revert_arguments_order(function_to_decorate):
    def revert_arguments_order_wrapper(*args, **kwargs):
        return function_to_decorate(*args[::-1], **kwargs)
    return revert_arguments_order_wrapper


@revert_arguments_order
def minus(a, b, c):
    return a - b - c


print(minus(5, 3, 1))


