def generate_n_bit_strings(n, bit_string=[]):
    if len(bit_string) == 2*n:
        if sum(bit_string[:n])==sum(bit_string[n:]):
            print(bit_string)
            return
    else:
        # Append '0' and explore
        generate_n_bit_strings(n, bit_string+[0])
        #Append '1' and explore
        generate_n_bit_strings(n, bit_string+[1])

# Example usage:
n = 2
generate_n_bit_strings(n)
