def format_text(text,prefix="",suffix="",capitalize=False,max_length=None):
    """
    format th input text with option prefix,suffix,capitalizeation and max_length
     parametrrs:
     text(str): the input text to be formed
     prefix(str,option):as addat string beginingof text
    suffix(str,optional): string to add at  the end of the text.defoult""
    capitalize(bool,optional):whether capitalize the text.
     max_length(int,option):maximum length of the final string
     return:
        srt: the formated string.
    raise:
         typeError: if input types are incorrect
         valuerror: if max length non positive

         example:
         >format_text("hello",prefix=")>>",suffix="<<"
         >hello<
    
    
    """
    #invalid input
    if not isinstance(text,str):
        raise TypeError("the  text paramete must be a string ")
    if not isinstance(prefix,str):
        raise TypeError(suffix,str)
    if not isinstance(suffix,str):
        raise TypeError("SUFFIX MUST BE A STRING")
    if not isinstance(capitalize, bool):
        raise TypeError("capitalize must be a boolean")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("maX Length must be inetrger")
        if max_length <= 0:
            raise ValueError("max length must be positive")
    if not isinstance(text, str):
        raise TypeError("the text must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("the prefix p[arameter must be astring .")
    if not isinstance(suffix, str):
        raise TypeError("the suffix parameter must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("Tthe capitalize must be booleann.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' must be an integer.")
        if max_length <= 0:
            raise ValueError("The 'max_length' must be a positive integer.")

    # capitalizatian text
    if capitalize:
        text = text.capitalize()

    # prefix and suffix
    formatted = f"{prefix}{text}{suffix}"

    # Alength restriction
    if max_length is not None:
        formatted = formatted[:max_length]

    return formatted


# test and prove the
if __name__ == "__main__":
    try:
        print(format_text("samuel", prefix=">>", suffix="<<"))
        print(format_text("samuel", capitalize=True))
        print(format_text("hello", max_length=3))
        print(format_text("bayishimire", prefix=">>", suffix="<<", capitalize=True, max_length=5))
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")



    


