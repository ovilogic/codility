import string


def solution(x):
    a_z = string.ascii_lowercase
    # The lowercase alphabet, in list form.
    a_z_list = list(a_z)
    # Another one that will be reversed. reverse() function changes the original instead of producing a new list.
    z_a_list = list(a_z)
    z_a_list.reverse()
    decoded_list = []
    # Iterating through the input text, one character at a time.
    for i in x:
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

solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")