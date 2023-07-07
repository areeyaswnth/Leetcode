class Solution:
    def interpret(self, command: str) -> str:
        str=''
        for i in range(0,len(command)):
            if(command[i]=='(' and command[i+1]==')'):
                str+='o'
            elif(command[i] not in '()'):
                str+=command[i]

        return str