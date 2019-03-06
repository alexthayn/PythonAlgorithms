from functools import lru_cache, reduce
from collections import namedtuple
SubProb = namedtuple('SubProb', ['value', 'partial', 'args'])


def knapval_rep(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are allowed"""

    # define and index all subproblems
    @lru_cache(maxsize=None)
    def knapv(w):
        subprobs = [(knapv(w-item.weight) + item.value)
            for item in items if item.weight <= w]
        return reduce(max, subprobs, 0)

    return knapv(capacity)


def knapval_norep_orig(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are not allowed"""

    @lru_cache(maxsize=None)
    def knapval(w, k):
        """returns max knapsack value with capacity of w choosing from first k items"""
        if k < 1:
            return 0
        # option 1) skip the last item
        options = [knapval(w, k-1)]
        # option 2) take the last item
        last_item = items[k-1]
        if last_item.weight <= w:
            options.append(last_item.value + knapval(w-last_item.weight, k-1))
        # return the best value
        return max(options)
    # the original problem is w is full capacity looking at all items
    return knapval(capacity, len(items))



# for edit_distance,
# rather than conditionally appending applicable sub problems to a list
# I'm going to use a paradigm described in https://stackoverflow.com/a/54939821/3780389
# I find it easier to describe the options that are available
# along with any conditions
Skip = object()
def drop_skipped(itr):
    return filter(lambda v: v is not Skip, itr)

# for example, here is how we might have used this
# idea with knapval_norep:
def knapval_norep(capacity, items):
    """returns the maximum value achievable in `capacity`
    weight using `items` when repeated items are not allowed"""

    @lru_cache(maxsize=None)
    def knapval(w, k):
        """returns max knapsack value with capacity of w choosing from first k items"""
        if k <= 0 or w <= 0:
            return 0
        options = drop_skipped([
            # skip the last item and then do your best
            knapval(w, k-1),
            # take the last item if it fits and then do your best
            items[k-1].value + knapval(w-items[k-1].weight, k-1) if items[k-1].weight <= w else Skip,
        ])
        # return the best value
        return max(options)
    # the original problem is w is full capacity looking at all items
    return knapval(capacity, len(items))


def edit_distance(s1, s2):
    """returns cost of the cheapest alignment between s1 and s2"""
    # define the sub problems in terms of prefix lengths
    @lru_cache(maxsize=None)
    def ed(i, j):
        """cost of aligning first i characters of s1 with first j
        characters of s2"""
        # in following comments, we will refer to p1 and p2 as
        # the prefixes to be aligned by this subproblem. i.e.:
        # p1 = s1[:i] # the first i chars of s1
        # p2 = s2[:j] # the first j chars of s2

        # one approach to the recursive definition is to list out
        # all of the options available along with constraints
        # that describe when each option is possible
        options = drop_skipped([
            # base case
            0 if i == 0 and j == 0 else Skip,
            # align last char of p1 with an inserted gap, so i is decremented but not j
            ed(i-1, j) + 1 if i > 0 else Skip,
            # align last char of p2 with an inserted gap, so j is decremented but not i
            ed(i, j-1) + 1 if j > 0 else Skip,
            # replace last char of p1 with last char of p2
            ed(i-1, j-1) + 1 if j > 0 and i > 0 and s1[i-1] != s2[j-1] else Skip,
            # align last char of p1 with matching last char of p2
            ed(i-1, j-1) if j > 0 and i > 0 and s1[i-1] == s2[j-1] else Skip
        ])
        return min(options)
    return ed(len(s1), len(s2))


# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])

def test_knapval_rep():
    loot = [
        Item(6, 30),
        Item(3, 14),
        Item(4, 16),
        Item(2, 9),
    ]
    assert knapval_rep(10, loot) == 48


def test_knapval_norep():
    loot = [
        Item(6, 30),
        Item(3, 14),
        Item(4, 16),
        Item(2, 9),
    ]
    assert knapval_norep(10, loot) == 46


def test_edit_distance():
    assert edit_distance("exponential", "polynomial") == 6

