def ceasar_cipher(ciphertext):
    alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
    len_alphabets = 26
    res = []
    for key in range(len_alphabets):
        plaintext = ''
        for ch in ciphertext:
            if ch in alphabets_upper:
                i = alphabets_upper.find(ch) - key
                plaintext = plaintext + alphabets_upper[i]
            elif ch in alphabets_lower:
                i = alphabets_lower.find(ch) - key
                plaintext = plaintext + alphabets_lower[i]
        
        res.append(plaintext)
    return res

if __name__ == '__main__':
    res = ceasar_cipher('SYNTPrfneVfPbbyOhgAbgFrpher')
    print(res[13])
