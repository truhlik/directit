def company_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<id>/<filename>
    return 'company_{0}/{1}'.format(instance.id, filename)


def first_letter_in_word(value: str) -> str:
    str_list = value.split(" ")

    if len(str_list) > 1:
        return str_list[0] + " {}*****".format(str_list[1][0] if len(str_list[1]) > 0 else "")
    if len(str_list) == 1:
        return str_list[0] + " *****"
    else:
        return "******"


def first_letter_name(value: str) -> str:
    if value is not None and len(value) > 1:
        return "".join([value[0], value[1:].replace(value[1:], "***")])
    else:
        return "***"
