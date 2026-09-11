def happy_hopper(sequence):
    sequence = []

    next_num = int(input("Enter the first number in the sequence: "))
    while next_num != -1:
        next_num = int(input("Enter the next number in the sequence (-1 to end): ")) # allow user to enter the sequence one number at a time
        sequence.append(next_num)
    
    if len(sequence) == 1:
        return True # any list of length 1 is a happy hopper

    main_seq = []
    comparison_seq = []

    for x in range(1, len(sequence)):
        num = abs(sequence[x] - sequence[x-1]) 
        main_seq.append(num) # adding the absolute value of the differences between each number in the sequence to one list...

    for x in range(1, len(sequence)):
        comparison_seq.append(x) # ...and all numbers from 1 to n-1 in another list (where n is the length of sequence)

    if sorted(main_seq) == sorted(comparison_seq): # checking to see if the absolute differences of sequence cover all numbers 1 to n-1
        return True
    else:
        return False