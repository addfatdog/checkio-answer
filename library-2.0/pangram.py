import string 
def check_pangram(text):
  return len([i for i in string.lowercase if i in text.lower()]) == 26

print check_pangram("The quick brown fox jumps over the lazy dog.") == True
print check_pangram("ABCDEF.") == False
