def print_ptr(ptr):
    for i in range(0, ptr):
        print(' ', end = '')
    print('|')

#INIT
def q0(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q0', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q0(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q0', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q1(tape, ptr, cntr)
    return

#FROM1STTO2ND
def q1(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q1', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q2(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q1', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q1(tape, ptr, cntr)
    return

#TO2NDSTART
def q2(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q2', cntr)
        print_ptr(ptr)
        ptr = ptr - 1
        q3(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q2', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q2(tape, ptr, cntr)
    return

#DECREMENT
def q3(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q3', cntr)
        print_ptr(ptr)
        ptr = ptr + 1
        q6(tape, ptr, cntr)
    elif tape[ptr] == '1':
        print(tape, end=' ')
        print('q3', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '0' + tape[ptr + 1:]
        ptr = ptr - 1
        q4(tape, ptr, cntr)
    elif tape[ptr] == '0':
        print(tape, end=' ')
        print('q3', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '1' + tape[ptr + 1:]
        ptr = ptr - 1
        q3(tape, ptr, cntr)
    return

#FROM2NDTO1ST
def q4(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q4', cntr)
        print_ptr(ptr)
        ptr = ptr - 1
        q5(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q4', cntr)
        print_ptr(ptr)
        ptr = ptr - 1
        q4(tape, ptr, cntr)
    return

#INCREMENT
def q5(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q5', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '1' + tape[ptr + 1:]
        ptr = ptr + 1
        q1(tape, ptr, cntr)
    elif tape[ptr] == '1':
        print(tape, end=' ')
        print('q5', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '0' + tape[ptr + 1:]
        ptr = ptr - 1
        q5(tape, ptr, cntr)
    elif tape[ptr] == '0':
        print(tape, end=' ')
        print('q5', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '1' + tape[ptr + 1:]
        ptr = ptr + 1
        q1(tape, ptr, cntr)
    return

#CLEAR
def q6(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q6', cntr)
        print_ptr(ptr)
        ptr = ptr - 1
        q7(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q6', cntr)
        print_ptr(ptr)
        tape = tape[:ptr] + '*' + tape[ptr + 1:]
        ptr = ptr + 1
        q6(tape, ptr, cntr)
    return

#GOTOEND
def q7(tape, ptr, cntr):
    cntr = cntr + 1
    if tape[ptr] == '*':
        print(tape, end=' ')
        print('q7', cntr)
        print_ptr(ptr)
        ptr = ptr - 1
        q7(tape, ptr, cntr)
    elif tape[ptr] == '1' or tape[ptr] == '0':
        print(tape, end=' ')
        print('q7', cntr)
        print_ptr(ptr)
        q8(tape, ptr, cntr)
    return

#END
def q8(tape, ptr, cntr):
    cntr = cntr + 1
    print(tape, end=' ')
    print('q8', cntr)
    print_ptr(ptr)
    return



q0(input(), 0, -1)