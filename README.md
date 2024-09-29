# 蓝桥杯生命之树题目见解
  写了几次都卡在第一个测试点，结果最后发现当输出是负数时，应该舍去输出0，感觉题目因该加上  **“当分数小于0时输出0”**
## 实现部分
使用defaultdict实现邻接表存储边的数据（~~记得导入from collections import defaultdict~~）
运用dp的思想求出以每一个节点为根节点的子树的最大分数，dp[i]=max(tree_value[i],tree_value[i]+max_list(mylist))。
用结果数组res存储每一次dp的值，注意res存储时应该存储tree_value[i]+max_list(mylist)，应为按题目理解S数组中元素个数应该大于2（~~额，不过第一次我加入dp[i]还是过了，数据好水~~）
