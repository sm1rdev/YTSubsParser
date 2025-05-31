def read_urls():
    url_list = []
    with open("input.txt", "r") as f:
        for line in f:
            url_list.append(line.strip())
    return url_list

def create_file(metadata, transcription:list):
    with open(f'data/{transcription[0]}_{transcription[1]}.txt', 'w', encoding="utf-8") as f:
        del transcription[:2]

        f.write(f"Название: {metadata['title']}\n")
        f.write(f"Описание: {metadata['description']}\n")
        f.write(f"Язык: {metadata['language']}\n")
        f.write(f"Теги: {metadata['tags']}\n")
        f.write("\n")
        f.write("Субтитры:\n")

        for line in transcription:
            f.write(f"{line}\n")