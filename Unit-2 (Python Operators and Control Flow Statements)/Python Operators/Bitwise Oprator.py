'''
    Write a program to implement betwise operator.
    Truth Table
            8  4  2  1
        ----------------
    0  =>   0  0  0  0
    1  =>   0  0  0  1
    2  =>   0  0  1  0
    3  =>   0  0  1  1
    4  =>   0  1  0  0
    5  =>   0  1  0  1
    6  =>   0  1  1  0
    7  =>   0  1  1  1
    8  =>   1  0  0  0
    9  =>   1  0  0  1
    10 =>   1  0  1  0
    11 =>   1  0  1  1
    12 =>   1  1  0  0
    13 =>   1  1  0  1
    14 =>   1  1  1  0
    15 =>   1  1  1  1

    
    Bitwise AND (&) =>
    7  =>    0 1 1 1
    14 =>    1 1 1 0
    ------------------
    7 & 14 =>0 1 1 0 = >6    



    Bitwise OR (|) =>
    7  =>    0 1 1 1
    14 =>    1 1 1 0
    ------------------
    7 | 14 =>1 1 1 1 = >15



    Bitwise (<<) left shift  =>
    7<<2
    we write 8 bit binary table
    7 = 0 0 0 0 0 1 1 1
    left shif =  0 0 0 1 1 1 0 0
    7<<2 = 28

    Bitwise (>>) rigth shift  =>
    7>>2
    we write 8 bit binary table
    7 =  0 0 0 0 0 1 1 1
    left shif =  0 0 0 0 0 0 0 1
    
    7>>2 = 1
'''

print(" Bitwise & :  7 & 14 =>", 7&14);
print(" Bitwise | :  7 | 14 =>", 7|14);
print(" Bitwise << : 7<<2 =>", 7<<2);
print(" Bitwise >> : 7>>2 =>", 7>>2);



