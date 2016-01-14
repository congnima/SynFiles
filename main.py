import synfiles
import sys
import time
import string


def main():
    src_dir = sys.argv[1]
    des_dir = sys.argv[2]

    print 'Analyzing ....\n\n'

    lst = list()
    lst =  synfiles.find_difference(src_dir,des_dir)

    print 'Analyze Complete!\n\n'
    
    #lst = list()

    if 0 != len(lst):
        print 'THESE FILES OR DIRECTORIES NEEDED BE COPIED:'
        for f in lst:
            print f
    else:
        print """THERE\'RE NO FILES OR DIRECTORIES NEEDED BE COPIED,THEY\'RE ALL THE SAME
              I AM GOING TO DIE IN FIVE SECONDS V_V...  
              """
        time.sleep(5)
        exit()

    
    choice = string.lower(raw_input('please confirm[y/n]:'))

    print '\n\n'

    if 'y' == choice:
        synfiles.do_copy(src_dir,des_dir,lst)
    else:
        exit()
    
    print '\n\nMission Complete!'

if __name__ == '__main__':
    main()