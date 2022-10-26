# ДНК представляет из себя последовательность (строку) из чередований четырёх молекул (букв): аденин (A), цитозин (C), гуанин (G), тимин (T). РНК же состоит из чередований аденина (A), цитозина (C), гуанина (G) и урацила (U). При транскрипции ДНК в РНК, аденин переходит в урацил, цитозин - в гуанин, гуанин - в цитозин, тимин - в аденин. Ваша задача написать функцию, которая по последовательности ДНК (например, 'AGCTAT') вычисляет последовательность РНК (соответственно 'UCGAUA').
def to_rna(dna_strand):
    dna_strand = dna_strand.replace('A','U').replace('G','K').replace('C','O').replace('T','A')
    dna_strand=dna_strand.replace('K','C').replace('O','G')
    return dna_strand # Удалите эту строку и напишите вместо неё ваш код
