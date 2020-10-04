import re

def is_palindrome(text):
    filtered_text = re.sub(r'\W', '', text.lower())
    reverse = filtered_text[::-1] 
    return reverse == filtered_text

print(is_palindrome('Nurses run.'))

print(is_palindrome('Dennis Sinned'))

print(is_palindrome('Roy, am I mayor?'))