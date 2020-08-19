# Bytesize
Bytesize is an old command-line tool for retreiving the correct answers to BBC Bitesize quizzes written in Python.

## What did it do

This tool was used to collate the answer page for any given BBC Bitesize answers for a given quiz.

The BBC Bitesize page has since been updated, so the tool no longer works.

## How it worked

It took a BBC Bytesize quiz URL and the number of questions on the page from user input.

It would first send an HTTP request to the quiz answer url with all the answers set to A and parse the resulting HTML determining which of the answers where correct. This is the repeated for B and C.

the correct answer
