def print_arguments(function_to_decorate):
    def print_arguments_wrapper(*args, **kwargs):
        res = function_to_decorate(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        return res
    return print_arguments_wrapper


@print_arguments
def minus(a, b, c):
    return a - b - c


print(minus(5, 3, 1))