
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        self.table.append(string)
        return

    def lookup(self, string):
        """Return the hash value if the
            string is already in the table.
            Return -1 otherwise."""
        n=len(self.table)
        for i in self.table:
            if i == string:
                return self.calculate_hash_value(string)
        return -1

    def calculate_hash_value(self, string):
        newstring = string[:2]
        hashvalue = ''
        for i in range(0,2,1):
            asciivalue = ord(newstring[i])
            hashvalue += str(asciivalue)
            
        return hashvalue
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print( hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
