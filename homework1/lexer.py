import sys
import re

tokens= {

    'var':      'VAR',
    'function': 'FUNCTION',
    'return':   'RETURN',
    'print':    'PRINT',
    'x':        'ASSIGN',
    '+':        'ADD',
    '-':        'SUB',
    '*':        'MULT',
    '/':        'DIV',
    '^':        'EXP',
    '(':        'LPAREN',
    ')':        'RPAREN',
    '{':        'LBRACE',
    '}':        'RBRACE',
    ',':        'COMMA',
    ':':        'COLON',
    }

IDENT=      '[a-zA-Z]+[a-zA-Z0-9_]*'
NUMBER=     '[+-]?((\d+(\.\d*)?)|(\.\d+))'
INDEX=      '[0-9]+'



def lexer( user_input, tokens):

    new_input=" "
    split_text= user_input.split(" ")
##    return split_text

 
##    find_RE1= re.findall(IDENT,split_text)
##    return find_RE1
    find_RE2= re.findall(INDEX,user_input)

    


    for i in split_text:
        if i in tokens:
            new_input += tokens[i]+ " "
            #return user_input


        else:
            if i in find_RE2:
                new_input += i.replace(i,"INDEX"+" ")
            

            else:
                new_input +="IDENT:"+i+ " "
                

       
    return new_input


def main():
    
   # while True:
    user_input= input( "lex: ")
    print(lexer(user_input, tokens))


if __name__=="__main__":

    main()



