import unicodedata
import pandas as pd
from unidecode import unidecode
import csv


df = pd.read_csv('fifa_players.csv', sep=',', encoding='utf-8')

def correct_characters(text):
    diacritic_characters = {
    'á', 'à', 'â', 'ä', 'ã', 'å', 'ā', 'ă', 'ą', 'ć', 'č', 'ç', 'ĉ', 'ċ', 'đ', 'ď', 'è', 'é', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě', 'ĝ', 'ğ', 'ġ', 'ģ', 'ĥ', 'ħ', 'ì', 'í', 'î', 'ï', 'ĩ', 'ī', 'ĭ', 'į', 'ı', 'ĳ', 'ĵ', 'ķ', 'ĸ', 'ĺ', 'ļ', 'ľ', 'ł', 'ñ', 'ń', 'ņ', 'ň', 'ŉ', 'ŋ', 'ò', 'ó', 'ô', 'ö', 'õ', 'ø', 'ō', 'ŏ', 'ő', 'œ', 'ŕ', 'ř', 'ś', 'š', 'ş', 'ŝ', 'ș', 'ť', 'ţ', 'ŧ', 'ù', 'ú', 'û', 'ü', 'ũ', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'ŵ', 'ŷ', 'ÿ', 'ź', 'ž', 'ż', 'ź', 'ż', 'ſ', 'Ά', 'Έ', 'Ή', 'Ί', 'Ϊ', 'ΐ', 'Ά', 'Έ', 'Ή', 'Ί', 'Ϊ', 'ΐ', 'ά', 'έ', 'ή', 'ί', 'ΐ', 'ΰ', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ϊ', 'ϋ', 'ό', 'ύ', 'ώ', 'ϕ', 'ϖ', 'ϗ', 'Ϙ', 'ϙ', 'Ϛ', 'ϛ', 'Ϝ', 'ϝ', 'Ϟ', 'ϟ', 'Ϡ', 'ϡ', 'ϰ', 'ϱ', 'ϲ', 'ϳ', 'ϴ', 'ϵ', '϶', 'Ϸ', 'ϸ', 'Ϲ', 'Ϻ', 'ϻ', 'ϼ', 'Ͻ', 'Ͼ', 'Ͽ', 'Ѐ', 'Ё', 'Ђ', 'Ѓ', 'Є', 'Ѕ', 'І', 'Ї', 'Ј', 'Љ', 'Њ', 'Ћ', 'Ќ', 'Ѝ', 'Ў', 'Џ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х'
                            }
    for char in diacritic_characters:
        text = text.replace(char, '')

    return text

#changes csv file because of diacritic_characters
df['name'] = df['name'].apply(correct_characters)
df['full_name'] = df['full_name'].apply(correct_characters)

df.to_csv('fifa_players_filtred.csv', index=False, encoding='utf-8', sep=';')
parameters_data = []

#17955
with open("fifa_players_filtred.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        new_row = {
            'Player': row['name'],
            'Player_full_name': row['full_name'],
            'Height': round(float(row['height_cm'])),
            'Weight': round(float(row['weight_kgs']))
        }
        parameters_data.append(new_row)