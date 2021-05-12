#!/usr/bin/python3
operation_stash = __import__("stats-operations")
operations = operation_stash.OPERATIONS
files = ['stats-' + operation + '.py' for operation in operations]
import subprocess


# open a subprocess with two-way communication
# if simply `"./stats-sum"` doesn't work, you can try
# passing the array `["python3", "./stats-sum"]`
for file in files:
    my_subprocess = subprocess.Popen(f"./{file}",
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for x in [1, 2, 3]:
        # need to encode the string, because we communicate binary
        # it needs a linebreak, because that is how we separate records
        my_subprocess.stdin.write("{}\n".format(x).encode('utf-8'))

    # inform the subprocess that is the end of input
    my_subprocess.stdin.close()

    # read the binary result, and decode
    # don't double the newlines
    print(f"Running {file} resulted in {my_subprocess.stdout.read().decode('utf-8')}", end='\n')
