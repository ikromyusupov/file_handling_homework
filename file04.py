def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for i in data:
        if i.isdigit()==False:
            ans.append(i)
    return ans
# Read data from file
fayl = open('txt_file/data03.txt', 'r')
data=fayl.read()