## username_generator.py
Script built to create a list of usernames to be used in bruteforcing attacks. Specially useful in conjunction with [Kerbrute](https://github.com/ropnop/kerbrute)

### Usage
```
usage: username_generator.py [-h] -w wordlist [-u]

Python script to generate user lists for bruteforcing!

optional arguments:
  -h, --help            show this help message and exit
  -w wordlist, --wordlist wordlist
                        Specify path to the wordlist
  -u, --uppercase       Also produce uppercase permutations. Disabled by default
```


### Example wordlist
```
root@kali:# cat example_wordlist.lst 
John Lennon
Lewis Hamilton
Iron Man
```


### Example output with lowercase permutations only
```
root@kali:# python3 username_generator.py -w example_wordlist.lst 
john
lennon
j.lennon
j-lennon
j_lennon
j+lennon
jlennon
lennonjohn
lewis
hamilton
l.hamilton
l-hamilton
l_hamilton
l+hamilton
lhamilton
hamiltonlewis
iron
man
i.man
i-man
i_man
i+man
iman
maniron

```


### Example output with lowercase and uppercase permutations
```
root@kali:# python3 username_generator.py -w example_wordlist.lst --uppercase
john
lennon
j.lennon
j-lennon
j_lennon
j+lennon
jlennon
lennonjohn
John
Lennon
J.Lennon
J_Lennon
J-Lennon
JLennon
LennonJohn
JOHN
LENNON
JOHNLENNON
....
```
