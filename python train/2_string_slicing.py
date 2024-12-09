# # strings slicing
# # string[start:end:step]

# text = "hello, World!"
# print(text[0:5])

# #basic slicing extracting substrings

# #omitting
# print(text[:5])

# print(text[7:])

# print(text[::2]) # takes every 2nd character

# print(text[1::2]) #output: 'el,wrd',
# # starts at index 1 and takes every 2nd character from there

# print(text[-6:-1]) # output:world
# #extracts characters from index -6 to -1

# print(text[::-1])
# # reverses the string by stepping backwards through it.

# text = "abcdefghij"
# print(text[1:9:3])
# # starts at index 1, goes up to (BUT NOT INCLUDING) index 9 taking every 3rd character.

# print(text[1:-1])
# # starts at index 1 and goes up to the last character

# print(text[8:2:-1])
# # starts at index 8 goes down to index 3 (but does not include it), in reverse order.

# print(text[5:5])
# # start and end are the same, so there's no range to extract.

# filename = "document.pdf"
# extension = filename[-3:] # output:'pdf'
# # slices the last 3 characters to get the file extension.

# print(extension)

# text = "hello"
# trimmed = text[1:-1] 
# print(trimmed)
# # removes the first and last character by slicing from index 1 to -1

# prefix = text[:2]
# suffix = text[-2:]

# print(prefix)
# print(suffix)




text = "hello wrold"
print(text[0:5])

print(text[:5])
print(text[7:])
print(text[::2])
print(text[1::2])

print(text[-6:-1])
print(text[::-1])


print(text[1:9:3])
print(text[1:-1])
print(text[8:2:-1])
print(text[8:2:-1])
print(text[5:5])







