import re

## Grouping with Parentheses
def MatchParentheses():
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group())
    print('Phone number found: ' + mo.group(1))
    print('Phone number found: ' + mo.group(2))

## Matching Multiple Groups with the Pipe '|'
def MatchMultipleGroup():
    heroRegex = re.compile(r'Batman|Tina Fey')

    mh = heroRegex.search('Tina Fey and Batman')
    print(mh.group())

## Optional Matching with the Question Mark
def MatchQuestion():
    batRegex = re.compile(r'Bat(wo)?man')

    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())

## Matching Zero or More with the Star
def MatchZero():
    batRegex = re.compile(r'Bat(wo)*man')
    
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())
    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo3.group())

## Matching One or More with the Plus
def MatchPlus():
    batRegex = re.compile(r'Bat(wo)+man')
    
    mo1 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    mo2 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo2.group())
    mo3 = batRegex.search('The Adventures of Batman')
    print(not(mo3 == None))

## Matching Specific Repetitions with Curly Brackets
def MatchSpecificRepetitions():
    haRegex = re.compile(r'(Ha){3}')
    mo1 = haRegex.search('HaHaHa')
    print(mo1.group())

    mo2 = haRegex.search('Ha')
    print(mo2 == None)
    
## Greedy and Nongreedy Matching
def GreedyVSNonGreedy():
    greedyHaRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyHaRegex.search('HaHaHaHaHa')
    print(mo1.group())

    nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
    mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
    print(mo2.group())

## Character Classes
def ShorthandCharacterClass():
    print(r'\d represents any numeric digit from 0 to 9')
    print(r'\D represents any character that is not a numeric digit from 0 to 9.')
    print(r'\w represents any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)')
    print(r'\W represents any character that is not a letter, numeric digit, or the underscore character.')
    print(r'\s represents any space, tab, or newline character. (Think of this as matching “space” characters.)')
    print(r'\S represents any character that is not a space, tab, or newline.')




