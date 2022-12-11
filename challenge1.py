import logging
import re
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



a_z = string.ascii_lowercase
a_z_list = list(a_z)
z_a_list = list(a_z)
print(a_z_list)
z_a_list.reverse()
print(a_z_list)


def decoder(text):
    decoded_list = []
    for i in text:
        if i in a_z_list:
            index = a_z_list.index(i)
            i = z_a_list[index]
            decoded_list.append(i)
        else:
            decoded_list.append(i)
    print(''.join(decoded_list))


decoder(doc)
decoder(doc2 )
