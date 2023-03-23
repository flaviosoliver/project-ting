def exists_word(word, instance):
    list = []
    words = []
    for index in range(len(instance)):
        file = instance.search(index)
        for line in file["linhas_do_arquivo"]:
            if word in line:
                words.append({"linha": index + 1})
        if len(words) > 0:
            file_word = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": words,
            }
            list.append(file_word)
    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
