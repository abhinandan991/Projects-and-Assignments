#getting input of text from the user
text=input("Text:")

#counting words, sentences and words in text provided
l,s,w=0,0,1

for i in range(len(text)):
    if text[i].isalpha():
        #counting letters
        l=l+1
    if text[i].isspace():
        #counting words
        w=w+1
    if text[i]=="." or text[i]=="?" or text[i]=="!":
        #counting sentences
        s=s+1

#counting average letters and sentences every 100 words
L=(l*100)/w
S=(s*100)/w

index = round(((0.0588 * L) - (0.296 * S) - 15.8))

#printing reading level
if index<1:
    print("Before Grade 1")
elif index>16:
    print("Grade 16+")
else:
    print("Grade ", index)