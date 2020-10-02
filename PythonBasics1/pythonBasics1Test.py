
import pythonBasics1
# main() is already set up to call the functions 
# we want to test with a few different inputs,
# printing 'OK' when each function is correct.
# the simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
  
# Calls the functions in pythonBasics1 with interesting inputs.
def main():
    # set which functions to test
    check_starts_with = True
    check_starts_with_vowel = True
    check_max_min_sum = True

    if check_starts_with:
        print('starts_with')
        test(pythonBasics1.starts_with('vest','v'), True)
        test(pythonBasics1.starts_with('crypt','c'), True)
        test(pythonBasics1.starts_with('#python','#'), True)
        test(pythonBasics1.starts_with('hello','H'), False)
        test(pythonBasics1.starts_with('',' '), False)
        test(pythonBasics1.starts_with('1',''), False)
        test(pythonBasics1.starts_with('',''), True)
        test(pythonBasics1.starts_with(' ',' '), True)
    
    if check_starts_with_vowel:
        print()
        print('starts_with_vowel')
        test(pythonBasics1.starts_with_vowel('vest'), False)
        test(pythonBasics1.starts_with_vowel('east'), True)
        test(pythonBasics1.starts_with_vowel('Eat'), True)
        test(pythonBasics1.starts_with_vowel('Ice'), True)
        test(pythonBasics1.starts_with_vowel('in'), True)
        test(pythonBasics1.starts_with_vowel('at'), True)
        test(pythonBasics1.starts_with_vowel('All'), True)
        test(pythonBasics1.starts_with_vowel('on'), True)
        test(pythonBasics1.starts_with_vowel('Out'), True)
        test(pythonBasics1.starts_with_vowel('unlock'), True)
        test(pythonBasics1.starts_with_vowel('Unique'), True)
        test(pythonBasics1.starts_with_vowel(''), False)

  
    if check_max_min_sum:
        print()
        print('max_min_sum')
        test(pythonBasics1.max_min_sum([1,2,3,4,5]),6)
        test(pythonBasics1.max_min_sum([3,2,5,4,6]),8)
        test(pythonBasics1.max_min_sum([-1,0,-3,-99,-2]),-99)
        test(pythonBasics1.max_min_sum([6]),6)
        test(pythonBasics1.max_min_sum([]),0)

if __name__ == '__main__':
  main()
