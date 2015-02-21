
def get_chunk(total, current, list):
    """

    :param total: Total number of wanted chunks
    :param current: Current chunk position wanted
    :param list: List of data who will be chunked
    :return: The chunk
    """
    length = len(list)//total
    start = current*length
    if current == total-1:
        return list[start:]
    return list[start:start+length]