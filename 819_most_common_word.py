'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.


Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.

'''
# my try 20200502
# failed because sometimes words are not split by ' ' but by punctuation, so in solution it used regex
def most_common_word (paragraph, banned):
    # input: para = string, banned = a list of strings 
    # output: a string (word), lower case
    # split the string to a list of words
    # process every word into lower case
    # iterate through the list, to add the not_banned words into a new list
    # iterate through the filtered list:
        # if the word is found more than once, then counter += 1 
        # the counter is a dictionary
    # find out the max of the value, and return the key

    import string 

    l1 = paragraph.split(' ')
    filtered_list = []
    for i in l1:
        i_transformed = ''.join(ch for ch in i if ch not in set(string.punctuation)).lower()
        if i_transformed not in banned: 
            filtered_list.append(i_transformed)
    counter = {}
    for i in filtered_list:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    l3 = list(counter.values())
    l4 = list(counter.keys())
    return l4[l3.index(max(l3))]

# solution
def most_common_word (paragraph, banned):
    import re
    word_list = re.split('\W+', paragraph.lower())

    max_freq,max_word, freq, banned_set  = 0, None, {}, set(banned)
    for word in word_list:
        if word not in banned_set:
            freq[word] = freq.get(word, 0) + 1
            if freq[word] > max_freq:
                max_freq, max_word = freq[word], word
    return max_word