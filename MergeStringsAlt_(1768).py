def Merge(word1,word2):
    i, j = 0,0              # Use 2 pointers to tsrat at the beginning of each word 

    new = []                # Use a list to store the combined words 

    while i < len(word1) and j < len(word2):    # Stop the loop until i is bigger than any word 
        new.append(word1[i])                    # Add evreything to the new list
        new.append(word2[j])

        i += 1                                  # Use a counter so it moves to the next word 
        j += 1

    new.append(word1[i:])                       # If there is anything leftover add it to the end of thew new list 
    new.append(word2[j:])

    return "".join(new)                         # Return the new word by combining evreything while turning it into a string 


word1 = "Sahar"                                 # Test code out 
word2 = "Karimi"

print(Merge(word1,word2))

                                                # Time Complexity: O(n+m)
                                                # Space Complexity: O(n+m)

                                        
    

