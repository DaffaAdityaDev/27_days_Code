from googletrans import Translator, LANGUAGES

trans = Translator()
t = trans.translate('bom dia')

print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')
