from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    censored_words = ['редиска']
    for word in censored_words:
        text = text.replace(word, '*' * len(word))
    return text
