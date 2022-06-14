def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans = []
    for i in data.split("\n"):
        ans.append(len(i))
    return max(ans)
# Read data from file
f = open('txt_file/data10','r')
data = f.read()