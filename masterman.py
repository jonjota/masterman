
class masterman:


    #def __init__(self):
    #    pass


    def reverse(self, input:str) -> str:

        return input[::-1]


    def atbash(self, input:str) -> str:

        '''
        This is the Atbash cypher, where we replace the letter A with the letter Z, the letter B with the letter Y and so on. In this cypher there is no mode to specify, as we only have to pass
        the input in order to obtain our desired result. For example, if we input the following code "EZIVMMVHHVIEZMGYVW" we will obtain "VARENNESSERVANTBED", and if we input "VARENNESSERVANTBED"
        we will obtain the cyphered version of the code "EZIVMMVHHVIEZMGYVW".
        '''

        cypher = ""

        for char in input:

          if char.isalpha():

            if char.isupper():


               offset =  25 - 2 * (ord(char) -  ord("A"))

               cypher += chr((ord(char) + offset  - ord('A'))  % 26 + ord('A'))

            else: 

               offset =  25 - 2 * (ord(char) -  ord("a"))

               cypher += chr((ord(char) + offset - ord('a'))  % 26 + ord('a')) 

          else:

              cypher += char

        return cypher







    def caesar(self, input: str, offset: int, mode: str = "decypher") -> str:   

        '''
        This is the Caesar cypher, where given an interger called offset, we shift the letters either forwards or backwards. The offset can be an arbitrary number, 
        but if we want to shift backwards, we need to specify the offset as a negative interger.  
        '''

        if mode != "decypher":

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





    def railfence(self, input: str, offset: int, rails: int, mode = "decypher") -> str:

        fence_rails = ["" for _ in range(rails)]
        
        if mode != "decypher":

            direction = "down"

            count = 0

            for char in input:

                if direction == "down": 

                    fence_rails[count] += char

                else: 

                    fence_rails[rails-1 - count ] +=char

                count += 1

                if count == rails-1 and direction == "down":

                    direction = "up"

                    count = 0

                elif count == rails-1 and direction == "up":

                    direction = "down"

                    count = 0

            cypher = ""

            for char_group in fence_rails:

                cypher += char_group


            return cypher


        asigned_rail = []

        for index, char in enumerate(input):

            if index == 0:

                





        return 0



 


if __name__ == "__main__":


    master = masterman()

    print(master.reverse(master.railfence("TRAVECYATTICPERONNE",0, rails = 5, mode = "cypher")))



 