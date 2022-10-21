
def req_steps(num_disks: int) -> int:
    """
    :param num_disks: number for n
    :return: return number of steps
    """

    # base case
    if num_disks == 1:
        return 1

    return 2 * req_steps(num_disks - 1) + 1


print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))
