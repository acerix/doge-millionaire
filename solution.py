
import random
from itertools import chain, izip

from pycoin.encoding import *
from pycoin.key import Key

# how many permutations to try in a row
max_permutations = 10

# break into chunks of these sizes
chunk_sizes_1 = [1,2,5,10,25]
chunk_sizes_2 = [2,5,10,25,50]


def answer(private_key, expected_address):

    private_key_digits = []

    for d in private_key:
        private_key_digits.append(BASE58_LOOKUP[d])

    #print(private_key)
    #print(private_key_digits)


    prefix = private_key_digits[0]
    suffix = private_key_digits[1:]
    test_suffix = tuple(suffix)

    if not private_key_suffix_is_valid(test_suffix):
        test_suffix = find_winner(tuple(suffix))

    print('WINNER!')
    private_key = b2a_base58(suffix_to_bytes(test_suffix))
    print(private_key)

    return Key.from_text(private_key).address()



def find_winner(suffix):
    """ Find a valid private key
    """

    while 1:

        test_suffix = tuple(suffix)
        print('')

        for i in range(max_permutations):

            test_suffix = tuple(random.choice(permutations)(test_suffix))

            if (private_key_suffix_is_valid(test_suffix)):
                return test_suffix

            print(b2a_base58(suffix_to_bytes(test_suffix)))




def suffix_to_bytes(s):
    """ Convert suffix digit list to key bytes
    """

    v = 5 # first digit
    for c in s:
        v *= 58
        v += c

    l = bytearray()
    while v > 0:
        v, mod = divmod(v, 256)
        l.append(mod)
    l.reverse()
    return bytes(l)



# memoize
keys_tried = set([])

def private_key_suffix_is_valid(private_key_digits):
    """ Determine if a private key is valid
    """

    # second char is always J/K?
    if private_key_digits[0] < 17 or 18 < private_key_digits[0]:
        return False

    # memoize
    key_hash = hash(private_key_digits)
    if key_hash in keys_tried:
        #print(len(keys_tried))
        return False
    keys_tried.add(key_hash)

    # convert to bytes
    r = suffix_to_bytes(private_key_digits)

    # verify checksum
    return r[-4:] == double_sha256(r[:-4])[:4]




def chunker(l, n):
    """ Yield successive n-sized chunks from l
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]



def swap_chunks(s):
    """ Swap first/last chunks
    """
    size = random.choice(chunk_sizes_1)
    chunks = list(chunker(s,size))
    a = 0
    b = len(chunks) - 1
    chunks[a], chunks[b] = chunks[b], chunks[a]
    return list(chain(*chunks))


def swap_all_chunks(s):
    """ Swap first with last, second with second last, etc
    """
    size = random.choice(chunk_sizes_1)
    chunks = list(chunker(s,size))
    last = 50/size - 1
    for a in range(last//2):
        b = last - a
        chunks[a], chunks[b] = chunks[b], chunks[a]
    return list(chain(*chunks))



def reverse_chunk(s):
    """ Reverse first chunk
    """
    size = random.choice(chunk_sizes_2)
    chunks = list(chunker(s,size))
    chunks[0] = chunks[0][::-1]
    return list(chain(*chunks))



def interleave_chunks(s):
    """ Interleave chunks
    """
    size = random.choice(chunk_sizes_2)
    chunks = list(chunker(s,size))
    return list(chain.from_iterable(izip(*chunks)))



def rotate_chunks(s):
    """ Move first chunk to the end
    """
    size = random.choice(chunk_sizes_2)
    #size = random.randrange(1,49)
    chunks = list(chunker(s,size))
    chunks.append(chunks.pop(0))
    return list(chain(*chunks))



def rotate_chunks_reverse(s):
    """ Move last chunk to the beginning
    """
    size = random.choice(chunk_sizes_2)
    #size = random.randrange(1,49)
    chunks = list(chunker(s,size))
    chunks.insert(0, chunks.pop())
    return list(chain(*chunks))


def swap_two(k):
    """ Swap two random chars
    """
    a = b = random.randrange(len(k))
    while a == b:
        b = random.randrange(len(k))
    t = list(k)
    t[a], t[b] = t[b], t[a]
    return tuple(t)





# which permutations to try
permutations = [
    swap_chunks,
    #swap_all_chunks,
    reverse_chunk,
    #interleave_chunks,
    rotate_chunks,
    rotate_chunks_reverse,
    #swap_two,
]
