def exists_word(word, instance):
    results = []

    for data in instance.data:
        occurences = []
        results.append({
            'palavra': word,
            'arquivo': data['nome_do_arquivo'],
            'ocorrencias': occurences
        })
        for index, line in enumerate(data['linhas_do_arquivo']):
            if word in line:
                occurences.append({'linha': index + 1})
        if not len(occurences):
            results.pop()

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
