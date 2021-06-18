def sortBoxes(boxList):
    # Write your code here
    # 1. split the box name by space
    old_version = []
    new_version = []
    for i in range(0, len(boxList)):
        box = boxList[i]
        box_array = box.split(" ")
        # 2. Check the version is old or new
        if box_array[1].isdigit():
            new_version.append(box)  # 2.a In original order
        else:
            id_len = len(box_array[0])
            old_version.append([box[:id_len], box[id_len:], i])
    # 3. sort the old version
    print(old_version)
    return 1


def validPoint(x, y, lot, flag):
    # Check if it is out of the grid
    if x < 0 or y < 0 or x >= len(lot) or y >= len(lot[0]):
        return False
    elif flag[x][y] == True or lot[x][y] == 0:
        return False
    else:
        return True


def distanceTraversed(lot):
    # Write your code here
    flag = [[False for j in range(len(lot[0]))] for i in range(len(lot))]
    print(flag)
    step_x = [0, 0, -1, 1]
    step_y = [1, -1, 0, 0]
    # Start from lot[0][0]
    # 1. set the start point [start y, start x, step to get here from start point, checked point or not]
    startPoint = [0, 0, 0]
    checking = [startPoint]
    flag[0][0] = True
    while len(checking) != 0:
        check_point = checking.pop(0)
        if lot[check_point[0]][check_point[1]] == 9:
            return check_point[2]
        else:
            # Check the four point around this point
            for i in range(0, 4):
                around_x = check_point[0] + step_x[i]
                around_y = check_point[1] + step_y[i]
                if validPoint(around_x, around_y, lot, flag):
                    flag[around_x][around_y] = True
                    checking.append([around_x, around_y, check_point[2] + 1])
    return -1

l=[[1,1,1,1], [0,1,1,1],[0,1,0,1],[1,1,9,1],[0,0,1,1]]
r = distanceTraversed(l)
print(r)
#l = ["yc 54"]
