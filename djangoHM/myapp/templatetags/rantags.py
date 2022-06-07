from django import template
import random
import string


register = template.Library()


@register.simple_tag()
def random_number(min_num, max_num):
    return random.randint(min_num, max_num)


@register.simple_tag()
def random_string(string_len):
    result = ''
    for i in range(string_len):
        result += (string.ascii_letters + string.digits)[random.randint(0, 61)]
    return result
