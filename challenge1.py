import logging
import string

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


'''
I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, 
you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know 
how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related 
notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] 
is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and 
punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the 
word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the
 commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.

Input:
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Input:
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!'''

doc = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
doc2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
doc3 = 'vmxibkgrlm'


def solution(s):
    a_z = string.ascii_lowercase
    # The lowercase alphabet, in list form.
    a_z_list = list(a_z)
    # Another one that will be reversed. reverse() function changes the original instead of producing a new list.
    z_a_list = list(a_z)
    z_a_list.reverse()
    decoded_list = []
    # Iterating through the input text, one character at a time.
    for i in s:
        # If character is in lowercase alphabet, take the index and use it to change the character to its counterpart
        # in the reversed alphabet.
        if i in a_z_list:
            index = a_z_list.index(i)
            i = z_a_list[index]
            decoded_list.append(i)
        # If any other character than lowercase alphabet, do nothing and add to the new list.
        else:
            decoded_list.append(i)
    # From list back to string.
    original_message = ''.join(decoded_list)
    print(original_message)
    return original_message


logging.debug('Start of function.')
solution(doc)
logging.debug('End of function.')
solution(doc2)
solution(doc3)