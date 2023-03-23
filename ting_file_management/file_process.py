import sys

from .file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(processed_data)
    sys.stdout.write(str(processed_data))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        remove = instance.dequeue()
        return sys.stdout.write(
            f"Arquivo {remove['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
