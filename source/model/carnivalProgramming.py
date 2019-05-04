#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 01:36
# @Author  : moiling
# @File    : carnivalProgramming.py

"""
游乐园路径规划问题

min g1(x) = ∑time(position_i, position_j)
min g1'(x) = time(position_door, position_first) + ∑time(position_i, position_j) + time(position_last, position_door)
min g1''(x) = time(position_door, position_first) + ∑time(position_i, position_j)
min g2(x) = ∑(start_time_i - current_time_i)
min G(x)  = g1(x) + g2(x)
    s.t. arrive_time_i <= end_time_i - stay_time_i

time =  | 0 2 3 1 |   => time[i][j] = time(position_i, position_j)
        | 2 0 4 2 |
        | 3 4 0 3 |
        | 1 2 3 0 |

start_time  = [stt1, stt2, stt3, stt4]  => start_time[i] = start_time_i
stay_time   = [sty1, sty2, sty3, sty4]  => stay_time[i]  = stay_time_i
end_time    = [end1, end2, end3, end4]  => end_time[i]   = end_time_i

i is the index of first_choose position
arrive_time[i] = start_time[i] || user_set_time

choose i->j
arrive_time[j] = arrive_time[i] + time[i][j] + stay_time[i]

如果是g1'(x)的话其实就是一个附加了条件的TSP问题
TSP问题求解用GA比较好，但是因为附加了条件，几乎没几个个体可以存活

如果是g1(x)或者g1''(x)的话其实就是贪婪找最近点
但是这个最近点应该是在一个优先面上找
优先面的意思是，a点必须在c前，b点必须在d前，那么ab就是优先面，也就是不需要前提条件的
可以用NSGA-II类似的方法求
如果算出冲突则回退，冲突的意思是a必须在c前，c必须在a前
"""


class Carnival:
    time = []
    start_time = []
    stay_time = []
    end_time = []
    arrive_time = []

    def __init__(self, time, start_time, stay_time, end_time):
        self.time = time
        self.start_time = start_time
        self.stay_time = stay_time
        self.end_time = end_time

    # 可以删了的方法
    def programming_without_start(self):
        """
        g1(x)的方式，没有出发点限制
        这个方法可以没有，用户自己设置i=0的情况就好了，主要是time[0][:]=time[:][0]=全0，说明每一个点都可以成为门，即可
        设这个方法完全是为了强制设为0
        :return: 同programming
        """
        # 这个有点麻烦，主要是non_domination和第一次递归的时候-1的问题，要把整体往后移一位就好了
        # 目前情况的话，就要把第0位给空出来，全0
        n = len(self.start_time)
        for pos in range(n):
            self.time[0][pos] = 0
            self.time[pos][0] = 0
        self.start_time[0] = 0
        self.stay_time[0] = 0
        self.end_time[0] = 0
        self.arrive_time = [-1] * n  # -1表示没有走过的点
        self.arrive_time[0] = 0
        i = 0
        # 先找出优先面，判断是否发生冲突
        conflict, front = self.non_domination_sort(i)
        if conflict:
            return False, front

        conflict, result = self.compute(i, front)
        result.reverse()  # 因为是递归，答案是反的
        return not conflict, result

    def programming(self):
        """
        g1''(x)的方式，其中门的位置为0
        :return:
            0th:ok
            1th:不ok：[[a,b],[c,d]]，ab冲突，cd冲突（二维数组）
                ok：[a,b,c]，abc为访问顺序（一维数组）
        """
        n = len(self.start_time)
        self.arrive_time = [-1] * n  # -1表示没有走过的点
        self.arrive_time[0] = self.start_time[0]  # 门的到达时间就是开始时间

        i = 0  # 出发点i是0，要计算终点j

        # 先找出优先面，判断是否发生冲突
        conflict, front = self.non_domination_sort(i)
        if conflict:
            return False, front

        conflict, result = self.compute(i, front)
        result.reverse()  # 因为是递归，答案是反的
        return not conflict, result

    def compute(self, i, front):
        """
        战术递归
        在当前front中找，找到了某一个可行的i就递归下去，如果front空了全都冲突，返回去到上一层，从i的后一个继续找
        如果全都找不到，就直接返回错误了
        最终节点因为front = []，所以不会循环，直接结束返回，将当前的下标链接到result中，一级一级返回
        当然还要判断是不是所有点都访问了，如果都访问了就是真的结束，不然还是算冲突
        下一级返回成功了说明战斗结束了，就不需要continue了，直接break
        :param i:
        :param front:
        :return:
            0th:是否冲突
            1th:如果冲突：[[a,b],[c,d]]，ab冲突，cd冲突（二维数组）
                如不冲突：[a,b,c]，abc为访问顺序（一维数组）
        """
        conflict = False
        conflict_result = []
        result = []

        # 终止条件
        if len(front) == 0:
            conflict = not self.is_all_visited()

        for j in front:  # 在front中找下一个点j
            self.arrive_time[j] = self.arrive_time[i] + self.stay_time[i] + self.time[i][j]
            # 先找出优先面，判断是否发生冲突
            conflict, front = self.non_domination_sort(j)
            if conflict:
                conflict_result = front
                # 还原
                self.arrive_time[j] = -1
                continue

            conflict, result = self.compute(j, front)
            if not conflict:
                break
            # 还原
            self.arrive_time[j] = -1

        # 到这里有两种情况，一种是要进入下一回合了，一种是把front走完了都没找到非冲突解
        if conflict:  # 还是冲突
            return True, conflict_result

        result.append(i)
        return False, result

    def non_domination_sort(self, start):
        """
        算优先面，arrive_time != -1的不参与，已经走过了
        :param start
        :return:
            0th:是否冲突
            1th:如果冲突：[[a,b],[c,d]]，ab冲突，cd冲突（二维数组）
                如不冲突：[a,b,c]，abc为优先面，按所需时间排序（一维数组）
        """
        result = []
        conflict = False
        n = len(self.start_time)
        end_time_of_start = self.stay_time[start] + self.arrive_time[start]
        position_n = [0] * n  # 这个地点被多少个支配
        # position_p = [[]] * n  # 这个地点支配了哪些地点

        for i in range(0, n - 1):
            if self.arrive_time[i] != -1:  # 跳过已访问节点
                continue

            for j in range(i + 1, n):
                if self.arrive_time[j] != -1:  # 跳过已访问节点
                    continue

                # 这里要计算是否需要等待
                temp_start_time = max(end_time_of_start + self.time[start][i], self.start_time[i])
                temp_start_time = max(temp_start_time + self.time[i][j] + self.stay_time[i], self.start_time[j])
                i_j = self.end_time[j] - self.stay_time[j] - temp_start_time

                temp_start_time = max(end_time_of_start + self.time[start][j], self.start_time[j])
                temp_start_time = max(temp_start_time + self.time[j][i] + self.stay_time[j], self.start_time[j])
                j_i = self.end_time[i] - self.stay_time[i] - temp_start_time

                if i_j < 0:  # 说明i不能在j前面进行，也就是j必须放在i前面
                    position_n[i] += 1
                    # position_p[j].append(i)
                if j_i < 0:  # 说明j不能在i前面进行，也就是i必须放在j前面
                    position_n[j] += 1
                    # position_p[i].append(j)
                if i_j < 0 and j_i < 0:  # 冲突啦
                    conflict = True
                    result.append([i, j])

        if not conflict:
            for i in range(0, n):
                if position_n[i] == 0 and self.arrive_time[i] == -1:
                    result.append(i)
            result = self.need_time_sort(start, result)

        return conflict, result

    def need_time_sort(self, start, select_index):
        select_time = []
        for i in select_index:
            # 要判断是否需要等待时间，不能直接用路程时间算，有可能去了还要等待
            wait_time = self.start_time[i] - self.arrive_time[start] - self.stay_time[start] + self.stay_time[i]
            no_wait_time = self.time[start][i] + self.stay_time[i]
            select_time.append(max(wait_time, no_wait_time))

        select = list(zip(select_index, select_time))
        select.sort(key=lambda x: x[1])

        return [x[0] for x in select]

    def is_all_visited(self):
        yes = True
        for i in self.arrive_time:
            if i == -1:
                yes = False
                break
        return yes

    def wrapper_result(self, result):
        wrapper = []

        for i in range(len(result)):
            wrapper.append({
                'position': result[i],
                'start_time': self.start_time[result[i]],
                'end_time': self.end_time[result[i]],
                'stay_time': self.stay_time[result[i]],
                'arrive_time': self.arrive_time[result[i]],
                'leave_time': max(self.arrive_time[result[i]], self.start_time[result[i]]) + self.stay_time[result[i]],
                'walk_time': 0 if i - 1 < 0 else self.time[result[i - 1]][result[i]],
                'wait_time': max(0, self.start_time[result[i]] - self.arrive_time[result[i]])
            })

        return wrapper