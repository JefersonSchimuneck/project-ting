import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(d['nome_do_arquivo'] == path_file for d in instance.data):
        return None

    file_content = txt_importer(path_file)
    file_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_content),
        'linhas_do_arquivo': file_content,
    }
    instance.enqueue(file_data)
    return print(file_data)


def remove(instance):
    if not len(instance.data):
        return print('Não há elementos')
    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
