import urllib.request

def answersPageGen(t, char, qs):
    page = t+"/answers?"
    for x in range(qs):
        page+="question"+str(x+1)+"="+char
        if x != qs-1:
            page+="&"
    return page
    

target = input("target: ")
questions = int(input("questions: "))
answers = []
for i in range(questions):
    answers.append("none")
alphabet = ["a","b","c"]
for n in range(3):
    testA = alphabet[n]
    answersPage = answersPageGen(target, testA, questions)
    #print(answersPage)
    with urllib.request.urlopen(answersPage) as response:
       html = response.read().decode()
       print(type(html))
       ans = html.split("correct-incorrect")
       for x in range(questions):
           if ans[x+1][2] == 'C':
               answers[x]=testA
       response.close()
print(answers)
