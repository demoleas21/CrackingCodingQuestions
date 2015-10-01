""" 1.6 String Compression """

def compressor(string):
    
    compression_table = {}
    for key in string:
        try:
            compression_table[key] = compression_table[key] + 1
        except:
            compression_table[key] = 1

    compressed_string = []
    for key in compression_table:
        compressed_string.append(key)
        compressed_string.append(str(compression_table[key]))
    final_string = "".join(compressed_string)
    if len(string) < len(final_string):
        return string
    else:
        return final_string

string = 'aabcccaa'
print(compressor(string))