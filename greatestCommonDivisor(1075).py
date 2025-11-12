def gcdOfStrings(str1, str2):
    from math import gcd                # Import The GCD function from math to use 

    if str1 + str2 != str2 + str1:      # Check if str1 + str2 and str2 + str1 are not the same when you combine them return nothing 
        return ""
    else:
        leng = gcd(len(str1), len(str2))    # If they are the same then get the lens 7 gcd of the lens 

        return str1[:leng]                  # return evreything before the len of str1 since were dividing by string1 
    


# Case 1:
print("Result Of First Case: ")
print(gcdOfStrings("ABCABC","ABC"))
print("\n")

# Case 2:
print("Result Of Second Case: ")
print(gcdOfStrings("ABABAB", "ABAB"))
print("\n")

# Case 3:
print("Result Of Third Case: ")
print(gcdOfStrings("LEET","CODE"))

