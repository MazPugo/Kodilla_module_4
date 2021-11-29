   # # function to check string is
# palindrome or not
def isPalindrome(str): # define function "isPalindrome"
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)): # use loop to check if the letters of the first half of the words are identical as the letters of the second half
        if str[i] != str[len(str)-i-1]: #Check if the index first and index last letters are not the same; Repeat step 2 by incrementing the first index and decrementing the last index.
            return False # if the mismatch is detected the return value will be false and we go out of the loop
    return True # if the word is palendrome the function will return true
 
# main function
s = "noon"
ans = isPalindrome(s)
 
if (ans):
    print("Yes") # print yes if the function is palendrome
else:
    print("No") # print no if the function is not palendrome
    