from django import template
import re

register = template.Library()


@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        return value  # Если значение не является строкой, просто верните его

    forbidden_words = ['редиска', 'блять', 'сволочь', 'скотина']

    for word in forbidden_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b',
                             re.I)  # ищем слово целиком без учета регистра и экранируем специальные символы
        value = pattern.sub('*' * len(word), value)

    return value


