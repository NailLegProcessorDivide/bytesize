# Bytesize
old tool for retreiving the correct answers to bbc bitesize quizes

## What did it do (broken site changed in past 5 years)

Used to retrieve the answer page for all posable bbc bytesize answers for a given quiz

## How it worked

It took a BBC Bytesize quiz URL and the number of questions on the page from STDIN.
It would then send an HTTP request to the quiz answer url with all the answers set to A then B then C.
the program would then extract the correct answers from the returned html and print those to STDOUT.
