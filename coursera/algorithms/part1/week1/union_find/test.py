from coursera.algorithms.part1.week1.union_find.quick_find import QuickFind
from coursera.algorithms.part1.week1.union_find.quick_union import QuickUnion
from coursera.algorithms.part1.week1.union_find.social_network_connectivity import SocialNetworkConnectivity
from coursera.algorithms.part1.week1.union_find.specific_canonical_element import SpecificCanonicalElement
from coursera.algorithms.part1.week1.union_find.successor_with_delete import SuccessorWithDelete

def test_successor_with_delete():
    swe = SuccessorWithDelete(10)
    assert swe.successor(1) == 2  # expected 2
    swe.remove(1)
    assert swe.successor(1) == 2  # expected 2
    swe.remove(3)
    assert swe.successor(2) == 4  # expected 3
    assert swe.successor(9) == 10  # expected 10

def test_specific_canonical_element():
    sce = SpecificCanonicalElement(10)
    sce.union(1, 2)
    sce.union(1, 3)
    sce.union(4, 6)
    sce.union(4, 7)
    sce.union(0, 2)
    assert sce.find(1) == 3  # expected 3
    assert sce.find(4) == 7  # expected 7

def test_social_network_connectivity():
    connectivity = SocialNetworkConnectivity(5)

    connectivity.union(1, 2, 1)
    connectivity.union(1, 3, 2)
    connectivity.union(0, 2, 5)
    connectivity.union(2, 3, 9)
    connectivity.union(0, 4, 11)

    assert connectivity.time == 11

def test_quick_union(n):
    qu = QuickUnion(n)
    qu.union(1, 2)
    qu.union(1, 3)
    assert qu.connected(2, 3) == True
    assert qu.connected(0, 3) == False

def test_quick_find(n):
    qf = QuickFind(n)
    qf.union(1, 2)
    qf.union(1, 3)

    assert qf.connected(2, 3) == True
    assert qf.connected(0, 3) == False

test_successor_with_delete()
test_specific_canonical_element()
test_social_network_connectivity()
test_quick_union(10)
test_quick_find(10)