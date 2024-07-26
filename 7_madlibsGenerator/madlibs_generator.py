
with open('7_madlibsGenerator/story.txt', encoding='utf-8') as f:
    story = f.read()

print(story)
words=set()
start_of_word=-1
target_strt="<"
target_end=">"
for i,char in enumerate(story):
    if char==target_strt:
        start_of_word=i
    if char==target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
        
answers={} 

for word in words:
    answer=input(f"Enter a word for {word}")
    answers[word]=answer
print(answers)
    
for word in words:
    story=story.replace(word,answers[word])
print(story)    
               
            
        
