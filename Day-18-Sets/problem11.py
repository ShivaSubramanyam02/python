english_speakers = {"John", "Emma", "Sophia", "Michael"}
french_speakers = {"Emma", "Lucas", "Sophia", "Chloe"}

multi_lang = english_speakers.intersection(french_speakers)
print(multi_lang)
single_lang = english_speakers ^ french_speakers
print(single_lang)