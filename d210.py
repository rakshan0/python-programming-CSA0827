def remove_common_words(s1, s2):
    
    words_s1 = set(s1.split())
    words_s2 = set(s2.split())
    
 
    common_words = words_s1 & words_s2
    
    
    words_s1 -= common_words
    words_s2 -= common_words
    
    
    updated_s1 = ' '.join(words_s1)
    updated_s2 = ' '.join(words_s2)
    
    return updated_s1, updated_s2


s1 = "sky is blue in color"
s2 = "Raj likes sky blue color"
updated_s1, updated_s2 = remove_common_words(s1, s2)
print(f"Updated S1: {updated_s1}")
print(f"Updated S2: {updated_s2}")
