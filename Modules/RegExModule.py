import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # The ^ and $ are anchors that match the start and end of the string, respectively.
# The .* matches any character (except for line terminators) zero or more times.
# The re.search() function searches the string for a match and returns a match object if found, otherwise None.
if x:
    print("YES! We have a match!")
else:
    print("No match")


x = re.findall("ai", txt) # The re.findall() function returns a list of all non-overlapping matches of the pattern in the string.
print(x) # ['ai', 'ai']

x = re.search(r'\s', txt) # The \s matches any whitespace character (spaces, tabs, newlines).
print(x.start())  

x = re.split(pattern=r"\s", string=txt, maxsplit=1) # The re.split() function splits the string at the occurrences of the pattern and returns a list.
print(x)

x = re.sub(r"\s", "9", txt) # The re.sub() function replaces the occurrences of the pattern in the string with the specified replacement.
print(x) 

x = re.sub(r"\s", "9", txt, count=2) # The count parameter specifies the maximum number of occurrences to replace.
print(x) # The count parameter specifies the maximum number of occurrences to replace.

x = re.search("ai", txt) # The re.search() function searches the string for a match and returns a match object if found, otherwise None.
print(x) 

x = re.search(r"\bS\w+", txt) # The \b matches the empty string at the beginning or end of a word.
print(x.span()) # The span() method returns a tuple containing the start and end positions of the match.
print(x.group()) # The group() method returns the string matched by the regular expression.
print(x.string) # The string attribute returns the string passed to the search() method.

