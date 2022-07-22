from myReplace import myReplace, myReplaceLetra, myReplacefor

word = input('Palabra: ')
newWord = myReplace(word,7,'u')
print(newWord)

word = input('Palabra: ')
newWord = myReplacefor(word,7,'o')
print(newWord)

word = input('Palabra: ')
newWord = myReplaceLetra(word,'i','a')
print(newWord)