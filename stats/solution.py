

def is_anagram(a, b):
    if a == b:
        return False

    if len(a) != len(b):
        return False
    
    if set(a) == set(b):
        return True
    
    return False


def stats(text):
    words = text.split()
    words_dict = {}
    most_recurrent_word = ''
    max_count = 0
    anagrams = []

    for i, w in enumerate(words):
        if not words_dict.get(w, False):
            words_dict[w] = 1
            
            for x in range(i + 1, len(words)):
                if words[x] not in words_dict.keys():
                    if is_anagram(w, words[x]):
                        anagrams.append([w, words[x]])
        else:
            words_dict[w] += 1
        
        if words_dict[w] > max_count:
            most_recurrent_word = w
            max_count = words_dict[w]

    return {
        'n_different_words': len(words_dict), 
        'most_recurrent_word': most_recurrent_word,
        'anagrams': anagrams,
    }


if __name__ == '__main__':
    text = 'hola si is no no'
    result = stats(text)
    msg = f"Number of different words: {result['n_different_words']}\nMost recurrent word: {result['most_recurrent_word']}\nAnagrams: {result['anagrams']}"
    print(msg)
    print('======================')
    assert result['n_different_words'] == 4

    text = 'in this example there are three types of trees and there are no hits'
    result = stats(text)
    msg = f"Number of different words: {result['n_different_words']}\nMost recurrent word: {result['most_recurrent_word']}\nAnagrams: {result['anagrams']}"
    print(msg)
