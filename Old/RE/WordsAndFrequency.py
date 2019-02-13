#!/usr/local/bin/python3
# Jordan Matuszewski
# 10 February 2019

import re
def main():

    string = open('X_Gentylnes_and_Nobylyte.txt', 'r').read()
    words = re.split('\W', string)
    dictionary_Sg = {}
    for word in words:
        if word:
            key = word.lower()
            if key in dictionary_Sg:
                dictionary_Sg[key] += 1
            else:
                dictionary_Sg[key] = 1
        else:
            pass
    keys = dictionary_Sg.keys()

    for key in keys:
        print("%2d\t%s" % (dictionary_Sg[key], key))

    #count of him
    count1 = dictionary_Sg['hym']
    print("Hym is present in the text",count1,"times.")

    #count of euer
    count2 = dictionary_Sg['euer']
    print("Euer is present in the text",count2,"times.")

    #count of wolde/wold
    count3 = dictionary_Sg['wolde'] + dictionary_Sg['wold']
    print("Wolde is present in the text",count3,"times.")

    #count of by/bi
    count4 = dictionary_Sg['by'] + dictionary_Sg['bi']
    print("By/bi is present in the text",count4,"times.")

    #count of his/hys
    count5 = dictionary_Sg['his'] + dictionary_Sg['hys']
    print("His/hys is present in the text",count5,"times.")

if __name__ == '__main__':
    main()
