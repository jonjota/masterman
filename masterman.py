
class masterman:


    #def __init__(self):
    #    pass



    def caesar(self, input: str, offset: int, mode: str = "cypher") -> str:   

        '''
        This is the Caesar cypher, where given an interger called offset, we shift the letters either forwards or backwards. The offset can be an arbitrary number, 
        but if we want to shift backwards, we need to specify the offset as a negative interger.
        '''

        if mode != "cypher":

            offset = - offset

        cypher = ""
            
        for char in input:

            if char.isalpha():

              if char.isupper():

                  cypher += chr((ord(char) + offset - ord('A'))  % 26 + ord('A'))

              else: 

                  cypher += chr((ord(char) + offset - ord('a'))  % 26 + ord('a')) 

            else:

                cypher += char

        return cypher


    def atbash(self, input:str, mode: str = "cypher") -> str:

        offset = 25

        if mode != "cypher":

            offset =  -offset

        cypher = ""

        for char in input:

           if char.isalpha():

             if char.isupper():

                 cypher += chr((ord(char) + offset - ord('A'))  % 26 + ord('A'))

             else: 

                 cypher += chr((ord(char) + offset - ord('a'))  % 26 + ord('a')) 

           else:

               cypher += char

        return cypher









        


if __name__ == "__main__":


    master = masterman()

    print(master.caesar("IHSSYVVTTHWCHYLUULZ", offset= 19))