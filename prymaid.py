#block 3
#line:3


#------------BLOCK 1 -------------
#line:1 ******
#line:2 ******
#line:3 ******
#line:4 ******
#line:5 ******
#25
#---------------------------------
#------------BLOCK 2 -------------
#line:1 ******
#line:2 ******
#line:3 ******
#line:4 ******
#20
#--------------------------------
#------------BLOCK3 -------------
#line:1 ******
#line:2 ******
#line:3 ******
#15

num_blocks = int(input("Enter number of blocks: "))
current_line = 1

for block in range(1, num_blocks + 1):
    print(f"#------------BLOCK {block} -------------")
    
    num_lines = int(input(f"Enter number of lines in BLOCK {block}: "))
    block_value = input(f"Enter value to print after lines in BLOCK {block}: ")
    
    for _ in range(num_lines):
        print(f"#line:{current_line} ******")
        current_line += 1
    
    print(f"#{block_value}")
    print("#" + "-" * 33)
