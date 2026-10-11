org_text=input("enter your text:")

if org_text.strip()=="":
    print("\n No text Entered \n")
else:
    text=org_text.lower()

    punc=".,!?()[]{}\':;"

    for i in punc:
        text=text.replace(i," ")

    words=text.split()
    print(words)
    count={}

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1


    long_word=words[0]

    for word in words:
        if len(word)>len(long_word):
            long_word=word

    most_freq=words[0]

    for  freq in count:
        if count[freq]>count[most_freq]:
            most_freq=freq

    search_word=input("enter word to search:").lower().strip()
    for i in punc:
        search_word=search_word.replace(i," ")

    count_word=count.get(search_word,0)

    print("="*40)
    print("           Text & Data Analyzer           ")
    print("="*40)
    print()
    print("Original Text:")
    print(org_text)
    print()
    print(f"Total words         :{len(words)}")
    print(f"Unique Words        :{len(set(words))}")
    print(f"Longest Word        :{long_word}")
    print(f"Most Frequent       :{most_freq}")
    print()
    print("Word Frequency:")
    for i in count:
        print(f"{i:<15}:{count[i]}")
    print()
    print("="*40)
    print("Search Word")
    print("="*40)
    print()
    if count_word>0:
        print(f"{search_word} appears {count_word} times")

    else:
        print(f"{search_word} was Not Found")
    print()
    print("="*40)