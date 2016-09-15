
def xor_strings(xs, ys):
     	return "".join(chr(ord(x) ^ ord(ys)) for x in xs)
