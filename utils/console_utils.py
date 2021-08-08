

def get_classname(args):
    split_args = args.split(' ')
    classname = split_args[0]
    return classname

def get_key_values(args):

    key_val = args[:].split(' ')
    del key_val[0]

    data = {}

    for s in key_val:
        key = s.split('=')[0].replace('"', '')
        value:str = s.split('=')[1].replace('"', '').replace(' ', '_')

        if value.isnumeric():
            value = int(value)

        elif '.' in value:
            value = float(value)
        data.update({key: value})
    return data
