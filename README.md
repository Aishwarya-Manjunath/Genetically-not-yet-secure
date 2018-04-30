# Genetically not yet Secure
This project was done as a part of the Computer network Security course.</n>
We have explored how Psuedo random Numbers can be easily predicted, and how we can increase the randomness of these numbers by applying concepts from the Genetic algorithm such as crossover and mutation. We have also looked into how crossover and mutation can also be applied for Symmetric Encryption and some attacks which can be done on the same.</n></n>


<b><n>Cracking Javas Random Library</b></n>

Present in the folder java_random. This includes how, given two numbers from Javas Random library it is easy to predict the following numbers. Javas Random library implements the Linear congruential generator.

The folder stattest_prng contains the code for applying crossover and mutation to the numbers obtained from the Linear Congruential Generator. It also contains some statistical tests which have been performed on the same. </n></n>


Reference : https://jazzy.id.au/2010/09/20/cracking_random_number_generators_part_1.html </n> </n>
 
<b>Encryption with Genetic Algorithm</b></n>

Paper referred: http://ijcsn.org/IJCSN-2017/6-3/Encryption-and-Decryption-Using-Genetic-Algorithm-Operations-and-Pseudorandom-Number.pdf

The basic implementation is present in the folder basic_implementation. This algorithm is extremely vulnerable to brute force attack especially when the input data is very less. The folder brute_force_attack_basic contains the code for bryte force attack.</n>

Brute force attack can be prevented for smaller inputs by increasing the length of the encrypted data. This implementation is present in the folder basic_improve. However it is still vulnerable to known input attacks especially when length of the input is known. The code for this attack is present in the folder known_input_attack.</n>

To prevent known input attacks, the position of the actual encrypted data can be varied. This is present in the folder improve_position.</n>

More developments can be done on this algorithm in order to make it crypto secure and importantly reduce the key size. 

To run the code for implementation of the Genetic Algorithm:</n>

python3 gui.py</n>


To run the code for attacks:</n>

python3 GA.py</n>
