def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    res = 0
    for i in data:
        if i.isdigit():
            i = int(i)
            if i > res:
                res = i
    return res
# Read data from file
f = open('txt_file/data08','r')
data = f.read()