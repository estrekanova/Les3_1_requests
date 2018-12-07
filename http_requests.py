# Вариант решения задачи для каждого файла в отдельности. Функция translate принимает следующие параметры:
# - Путь к файлу с текстом;
# - Путь к файлу с результатом;
# - Язык с которого перевести;
# - Язык на который перевести (по-умолчанию русский).
import requests
url = 'https://translate.yandex.net/api/v1/tr.json/translate'


def translate(read_file, write_file, lang_source, lang_result='ru', ):
    params = {'id': 'bbb166d1.5c0823ba.a93a2094-4-0',
              'srv': 'tr-text',
              'lang': '-'.join([lang_source, lang_result]),
              'reason': 'paste'}
    write_text = list()
    try:
        with open(read_file, 'r', encoding='utf-8') as f:
            for line in f:
                response = requests.post(url=url, data={'text': line}, params=params).json()
                write_text.append(' '.join(response.get('text', [])))
                assert response.get('text') != None, ''.join(response.get('message', []))
    except FileNotFoundError:
        return f'Файл {read_file} не найден'
    except AssertionError as e:
        return e
    except requests.exceptions.ConnectionError:
        return 'Connection Error'

    try:
        with open(write_file, 'w', encoding='utf-8') as f:
            for line in write_text:
                f.write(line)
    except FileNotFoundError:
        return f'Ошибка доступа к файлу {write_file}'
    return f'Перевод завершен. Результат сохранен в файл {write_file}'


if __name__ == '__main__':
    while True:
        if input('Для выхода введите "e". Для продолжения нажмите Enter: ').lower() == 'e':
            break
        source_file = input('Введите полное имя файла для перевода (например, d:/file.txt): ')
        if source_file == '':
            print('Не указано имя файла для перевода\n')
            continue
        result_file = input('Введите полное имя файла для сохранения перевода (например, d:/rus.txt): ')
        if result_file == '':
            print('Не указано имя файла для сохранения перевода\n')
            continue
        source_lang = input('Введите язык исходного текста (например, en - английский, fr - французский): ')
        if source_lang == '':
            print('Не указан язык исходного текста\n')
            continue
        result_lang = input('Введите язык перевода или нажмите Enter для перевода на русский: ')
        if result_lang == '':
            print(translate(source_file, result_file, source_lang))
        else:
            print(translate(source_file, result_file, source_lang, result_lang))
