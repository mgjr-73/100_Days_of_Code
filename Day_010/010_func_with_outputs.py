# Functions with Outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("john", "jones")
print(formatted_string)

# Or to simplify...

print(format_name("john", "jones"))