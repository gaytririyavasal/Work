
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Chris has to complete a programming assignment overnight. He has to write n lines of code before morning.
He is dead tired and he tries drinking some black coffee to keep him awake. But each time he drinks a cup
of coffee he stays awake for a short amount of time but his productivity goes down by a constant factor k.

This is how he plans to write the program. He will write the first v lines of code, then drink his first cup
of coffee.

• Since his productivity has gone down by a factor of k he will write v // k lines of code.

• He will have another cup of coffee and then write v // k**2 lines of code.

• He will have another cup of coffee and write v // k**3 lines of code and so on.

• He will collapse and fall asleep when v // k ** p becomes 0.

Now, Chris does want to complete his assignment and maximize on his sleep. So he wants to figure out
the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines
of code before he falls asleep.

Input:

You will read your input from standard input as given in the following format file work.in:

2
300 2
359 9

The first line is T the number of test cases. This will be followed by T lines of input. Each line of input
will have two numbers nand k. nis the number of lines of code to write and kis the productivity factor,
where 1 ≤n≤106and 2 ≤k≤10.

Output:

For each test case write your result to standard out as shown in file work.out. In your output there will be
v lines of code the Chris has to write, as well as the time it took for each function. For the above two test
cases, the output will be:

Binary Search: 152
Time: 9.512901306152344e−05

Linear Search: 152
Time : 0.0005910396575927734

Binary Search: 54
Time: 4.696846008300781e−05

Linear Search: 54
Time: 9.012222290039062e−05

Do not worry if your times do not match ours exactly. They are given just for comparison purposes. For
this assignment, main has been written completely for you, and nothing needs to be changed in it.

You will be solving this problem in 2 ways. First, you will write a function that uses a linear search to
solve the problem. Then you will write a function that uses a modified binary search algorithm to solve it
again. Both functions will return the same answer, but the binary search method will usually be faster.

It is recommended that you write a helper function, which given a value v representing the number of
lines Chris writes before his first cup of coffee and a value k, the productivity factor, will calculate the
number of lines Chris will write before falling asleep. This can be called in both the linear and binary
functions to make the computations easier.
