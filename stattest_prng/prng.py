#current local time (32-bit number)
import os
import time
seed1 = int(time.time())		#the time seed


#LCG and generate 16 random numbers
def lcg():
    a = 1140671485
    c = 128201163
    m = 2**32
    global seed1
    seed1 = (a*seed1 + c) % m
    return seed1

bit512=''
for i in range(16):
	a=lcg()
	val= bin(a)[2:].zfill(32)	#convert variable length bin rand to 32 bit each
	bit512+=val

#print bit512,'\n\n',len(bit512)			#512 bit number

not_bit512 = ''.join('1' if x == '0' else '0' for x in bit512)

#print not_bit512

pt_crsvr=bin(os.getpid())[2:].count('1')	#point of crossover


# crossover function
def crsvr(a,b,n):
	nn=n
	flag=1
	out=''
	while(nn<len(a)):
		if(flag==1):
			out+=a[nn-n:nn]
			flag=2
		else:
			out+=b[nn-n:nn]
			flag=1
		nn+=n
	if (flag==1):
		out+=a[nn-n:512]
	else:
		out+=b[nn-n:512]
	return out

op= crsvr(bit512,not_bit512,pt_crsvr)

#print op,'\n'
#print bit512,'\n'

#mutation function, XOR is user here
final_op = ''.join('1' if op[x]=='0' else '0' for x in range(512))
final_op1 = ''.join('1' if bit512[x] != op[x] else '0' for x in range(512))

import math
import numpy
from scipy import special as spc
def longest_runs(bin_data):
    """
    Note that this description is taken from the NIST documentation [1]
    [1] http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf
    The focus of the tests is the longest run of ones within M-bit blocks. The purpose of this tests is to determine
    whether the length of the longest run of ones within the tested sequences is consistent with the length of the
    longest run of ones that would be expected in a random sequence. Note that an irregularity in the expected
    length of the longest run of ones implies that there is also an irregularity ub tge expected length of the long
    est run of zeroes. Therefore, only one test is necessary for this statistical tests of randomness
    :param bin_data: a binary string
    :return: the p-value from the test
    """
    if len(bin_data) < 128:
        print("\t", "Not enough data to run test!")
        return -1.0
    elif len(bin_data) < 6272:
        k, m = 3, 8
        v_values = [1, 2, 3, 4]
        pik_values = [0.21484375, 0.3671875, 0.23046875, 0.1875]
    elif len(bin_data) < 75000:
        k, m = 5, 128
        v_values = [4, 5, 6, 7, 8, 9]
        pik_values = [0.1174035788, 0.242955959, 0.249363483, 0.17517706, 0.102701071, 0.112398847]
    else:
        k, m = 6, 10000
        v_values = [10, 11, 12, 13, 14, 15, 16]
        pik_values = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]

    # Work out the number of blocks, discard the remainder
    # pik = [0.2148, 0.3672, 0.2305, 0.1875]
    num_blocks = len(bin_data) // m
    frequencies = numpy.zeros(k + 1)
    block_start, block_end = 0, m
    for i in range(num_blocks):
        # Slice the binary string into a block
        block_data = bin_data[block_start:block_end]
        # Keep track of the number of ones
        max_run_count, run_count = 0, 0
        for j in range(0, m):
            if block_data[j] == '1':
                run_count += 1
                max_run_count = max(max_run_count, run_count)
            else:
                max_run_count = max(max_run_count, run_count)
                run_count = 0
        max_run_count = max(max_run_count, run_count)
        if max_run_count < v_values[0]:
            frequencies[0] += 1
        for j in range(k):
            if max_run_count == v_values[j]:
                frequencies[j] += 1
        if max_run_count > v_values[k - 1]:
            frequencies[k] += 1
        block_start += m
        block_end += m
    # print(frequencies)
    chi_squared = 0
    for i in range(len(frequencies)):
        chi_squared += (pow(frequencies[i] - (num_blocks * pik_values[i]), 2.0)) / (num_blocks * pik_values[i])
    p_val = spc.gammaincc(float(k / 2), float(chi_squared / 2))
    return p_val

print "Runs Test"
print "LCG"
print longest_runs(bit512)
print "With Genetic: (Mutuation : not)"
print longest_runs(final_op)
'''
print "With Genetic: (Mutation : XOR)"
print longest_runs(final_op1)
'''

import skidmarks as sk
''''
print "-------------------------------------------------------------"
print "Gaps Test"
print "LCG"
print sk.gap_test(bit512)['p']
print "With Genetic: (Mutuation : not)"
print sk.gap_test(final_op)['p']
print "With Genetic: (Mutation : XOR)"
print sk.gap_test(final_op1)['p']
'''

print "-------------------------------------------------------------"
print "Autocorrelation Test"
print "LCG"
print sk.auto_correlation(bit512)['p']
print "With Genetic: (Mutuation : not)"
print sk.auto_correlation(final_op)['p']
'''
print "With Genetic: (Mutation : XOR)"
print sk.auto_correlation(final_op1)['p']
'''

'''
print "-------------------------------------------------------------"
print "Serial Test"
print "LCG"
print sk.serial_test(bit512)['p']
print "With Genetic: (Mutuation : not)"
print sk.serial_test(final_op)['p']
print "With Genetic: (Mutation : XOR)"
print sk.serial_test(final_op1)['p']



print "-------------------------------------------------------------"
print "Wald_wolfowitz Test"
print "LCG"
print sk.wald_wolfowitz(bit512)['p']
print "With Genetic: (Mutuation : not)"
print sk.wald_wolfowitz(final_op)['p']
print "With Genetic: (Mutation : XOR)"
print sk.wald_wolfowitz(final_op1)['p']
'''


def monobit(bin_data):
    """
    Note that this description is taken from the NIST documentation [1]
    [1] http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf
  
    The focus of this test is the proportion of zeros and ones for the entire sequence. The purpose of this test is
    to determine whether the number of ones and zeros in a sequence are approximately the same as would be expected
    for a truly random sequence. This test assesses the closeness of the fraction of ones to 1/2, that is the number
    of ones and zeros ina  sequence should be about the same. All subsequent tests depend on this test.
  
    :param bin_data: a binary string
    :return: the p-value from the test
    """
    count = 0
    # If the char is 0 minus 1, else add 1
    for char in bin_data:
        if char == '0':
            count -= 1
        else:
            count += 1
    # Calculate the p value
    sobs = count / math.sqrt(len(bin_data))
    p_val = spc.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val

print "-------------------------------------------------------------"
print "Monobit Test"
print "LCG"
print monobit(bit512)
print "With Genetic: (Mutuation : not)"
print monobit(final_op)
'''
print "With Genetic: (Mutation : XOR)"
print monobit(final_op1)
'''

