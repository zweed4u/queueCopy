import sys
import os
import time

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


'''
def countLetterOpenFile(filename):
    ins = open( filename, "r" )
    array = []
    for line in ins:
        array.append( line )
    ins.close()
'''




def main():
    print "\n"
    print'                                             888 88e                  d8            ' 
    print' e88 888 8888 8888  ,e e,  8888 8888  ,e e,  888 888D  ,"Y88b  dP"Y  d88    ,e e,   '
    print'd888 888 8888 8888 d88 88b 8888 8888 d88 88b 888 88"  "8" 888 C88b  d88888 d88 88b  '
    print'Y888 888 Y888 888P 888   , Y888 888P 888   , 888      ,ee 888  Y88D  888   888   ,  '
    print' "88 888  "88 88"   "YeeP"  "88 88"   "YeeP" 888      "88 888 d,dP   888    "YeeP"  '
    print'     888                                                                            '
    print'     888                                                                            '
    print'             ######         #   ####### #     #                      #       #     #' 
    print'             #     # #   # ###       #  #  #  # ###### ###### #####  #    #  #     #'
    print'             #     #  # #   #       #   #  #  # #      #      #    # #    #  #     #'
    print'             ######    #           #    #  #  # #####  #####  #    # #    #  #     #'
    print'             #     #   #    #     #     #  #  # #      #      #    # ####### #     #'
    print'             #     #   #   ###   #      #  #  # #      #      #    #      #  #     #'
    print'             ######    #    #   #######  ## ##  ###### ###### #####       #   ##### '


    print "\n"
    try:
        filename = raw_input("Please Enter the filename along with its extension: ")
        print "\n"
        
        #countLetterOpenFile(filename)


        ins = open( filename, "r" )
        array = []

        
        for line in ins:
            array.append( line )
        ins.close()

        
        
        i=0
        while i<len(array):
            print "In clipboard: " +str(array[i].rstrip('\n'))
            addToClipBoard(str(array[i]))
            #raw_input("Press Enter after you've pasted...\n")   #set to time delay so you have x amount of seconds to paste 
            print('"'+str(array[i].rstrip('\n'))+'"' + " will remain in the clipboard for 5 seconds before next element.\n")
            time.sleep(5)
            i+=1
            
        print "\n"



        
        raw_input("Please Hit Enter to End")
        print "\n"
        sys.exit
    except:
        
        print "~~~Fatal Error~~~\n"
        print ">> FileIO issues: <<"
        
        print "- Could not find file with specified name."
        print "- Remember to include extension in input and have file in queue.py's folder."
        print "\n"

os.system('cls' if os.name == 'nt' else 'clear')
main()
