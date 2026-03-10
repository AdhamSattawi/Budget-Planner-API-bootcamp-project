def type_check(func):
    """This function validate that both the inputs and the output of the function 
        match the provided type annotations, raising a TypeError if they do not."""
    def wrapper(*args, **kwargs):
        arg_type_dict = func.__annotations__
        if not supported_types(arg_type_dict):
            return func(*args, **kwargs)
        kwarg_check(kwargs, arg_type_dict)
        args_check(args, arg_type_dict)
        return_type = arg_type_dict["return"]
        func_output = func(*args, **kwargs)
        if not isinstance(func_output, return_type):
            raise TypeError()
        return func_output

    return wrapper


def supported_types(arg_type: dict) -> bool:
    supported_types = [int, float, str, list, dict, bool, type(None)]
    for arg in arg_type:
        if arg_type[arg] not in supported_types:
            return False
    return True


def kwarg_check(kwargs: dict, arg_type_dict: dict) -> None:
    for arg in kwargs:
        if arg in arg_type_dict:
            if not isinstance(kwargs[arg], arg_type_dict[arg]):
                raise TypeError(f"Argument '{arg}' must be {arg_type_dict[arg]}")


def args_check(args: tuple, arg_type_dict: dict) -> None:
    name_list = [key for key in arg_type_dict.keys() if key != "return"]
    for arg, name in zip(args, name_list):
        type_expected = arg_type_dict[name]
        if not isinstance(arg, type_expected):
            raise TypeError(f"Argument '{arg}' must be {arg_type_dict[arg]}")
