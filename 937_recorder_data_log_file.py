'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''

# Liyou: 20200503
# I assumed that identifier is either "let" or "dig"

def recorder_log_files(logs):
    # input: an array of strings
    # output: a sorted array of strings
    # separate the logs into let logs and dig logs
    # for let logs, ignore the identifier, order the rest lexically 
        # split by ' ' --> a list of 

    # for dig logs, keep the original order
    # combine the let logs and dig logs into one array
    let_logs = []
    dig_logs = []
    for i in logs:
        if i.split(' ')[1].isdigit():
        # if type(i.split(' ')[1]) == str: # note not 'str' or 'string' --> doesn't work, everything is a string
            # if i[:3] == 'let': #note! my first try [:2]
            let_logs.append(i)
        else:
            dig_logs.append(i)
    dic = {}
    for i in let_logs:
        identifier = i.split(' ')[0]
        rest = ' '.join (ch for ch in i.split(' ')[1::])
        dic[rest] = identifier
    rest_list = list(dic.keys())
    rest_list.sort() #sorted 
    let_logs_sorted = []
    for i in rest_list:
        let_logs_sorted.append(dic[i] + ' '+ i) # identifier + ' ' + rest 
    let_logs_sorted.extend(dig_logs)
    return let_logs_sorted



#  solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []      # list for 'digit logs'
        string_logs =[]      # list for 'string logs'
        result=[]            # a special list for result
# ------
# Let's split logs by spaces and sort them out in two buckets
	   for _ in logs: 
            split_it=_.split(" ") # split current log 
            if split_it[1].isdigit(): # check if digits in log
                digit_logs.append(" ".join(split_it[:]))  # add as a string
            else: # hence, it strings log
                # add log id and digits separately
                string_logs.append([split_it[0]," ".join(split_it[1:])])
       
# Okay, lets collect the result back
# ----------
# first add strings to the result being sorted with 
# two keys: firstly sort by string_logs[1], then by string_logs[0]
        for i in sorted(string_logs,key=operator.itemgetter(1, 0)): 
            result.append(" ".join(i)) # rejoin back to simple string
        return result + digit_logs

O(nlog n)
Space O(3n)