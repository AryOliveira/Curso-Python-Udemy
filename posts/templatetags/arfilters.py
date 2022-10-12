from django import template

register = template.Library()

@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentario):
    try:
        num_comentarios = int (num_comentario)

        if num_comentarios == 0:
            return f'Nenhum comentário!'
        elif num_comentarios == 1:
            return f'{num_comentarios} Comentário!'
        else:
            return f'{num_comentarios} Comentários!'
    except:
        return f'{num_comentario} COMENTARIO(S)'
