def load_data(file) :
    with open(file) as file:
        lines = file.readlines()
    data = ([s.replace('\n', '') for s in lines])
    return data

def load_stats(data) :
    stats = {}
    t = 0
    for word in data:
        for letter in word:
            if letter in stats :
                stats[letter] += 1
            else :
                stats[letter] = 1
            t += 1
    for key, value in stats.items():
        stats[key] = round(value * 100 / t,4)
    return stats

def starting_with(letter,data):
    return list(filter(lambda x:x[0]==letter, data))

def letter_not_in_word(wrong_guess,data) :
    wrong_guess = [char for char in wrong_guess]
    for l in wrong_guess :
        data = list(filter(lambda x: l not in x, data))
    return data

def word_size(size,data):
    return [x for x in data if len(x)==size]

def known_letter(word,data):
    to_delete = []
    i = 0
    for letter in word :
        if letter != '?':
            for w in data :  
                if w[i] != letter :                
                    to_delete.append(w)
        i += 1
    return list(set(data) - set(to_delete))


def best_proposition(data, stats) :
    s = 0
    best_score = 0
    proposition = ""
    for word in data:
        for letter in set(word) :
            s += stats[letter]
        if s > best_score:
            proposition = word
    return proposition                   


if __name__ == '__main__':  
    stats = {}  
    while True:        
        data = load_data('data.txt')
        if not stats :
            stats = load_stats(data)
        first_letter = input("Premiere lettre : ")
        if first_letter == '!!' or first_letter == '!' :
            exit()        
        word_length = input("longueur du mot : ")
        if word_length == '!!' or word_length == '!':
            exit()
        data = starting_with(first_letter,data)     
        data = word_size(int(word_length), data)
        not_a_letter = ""
        print(best_proposition(data, stats))
        opt = ''
        while opt != 's' or opt != 'v':
            print('-' * 10)
            opt = input("Supprimer (s) ou valider (v) des lettres : ")
            if opt == '!' :
                break
            if opt == '!!' :
                exit()                    
            if opt == 's' :
                not_a_letter = input("Lettre non presente dans le mot : ")
                if not_a_letter == '!' :
                    break    
                if not_a_letter == '!!' :
                    exit()
                data = letter_not_in_word(not_a_letter,data)
            if opt == 'v' :
                is_a_letter = input("Saisir le mot avec des joker (bo?j?ur) : ")
                if is_a_letter == '!' :
                    break    
                if is_a_letter == '!!' :
                    exit()
                data = known_letter(is_a_letter,data)
            print(best_proposition(data, stats))
        print('-' * 20)