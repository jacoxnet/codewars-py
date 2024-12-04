def unique_in_order(sequence):
    test_prior = False
    prior = ""
    ret_seq = []
    for elem in sequence:
        if test_prior:
            if elem != prior:
                ret_seq.append(elem)
        else:
            ret_seq.append(elem)
        test_prior = True
        prior = elem
    return ret_seq


import codewars_test as test

@test.describe("Sample Tests")
def sample_tests():
    @test.it("Should work with empty sequence")
    def _():
        test.assert_equals(unique_in_order(""), [])
        test.assert_equals(unique_in_order([]), [])
        test.assert_equals(unique_in_order(()), [])

    @test.it("Should work with single element sequence")
    def _():
        test.assert_equals(unique_in_order("A"), ["A"])
        test.assert_equals(unique_in_order(["A"]), ["A"])
        test.assert_equals(unique_in_order(("A",)), ["A"])

    @test.it("Should reduce duplicates")
    def _():
        test.assert_equals(unique_in_order("AA"), ["A"])
        test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

    @test.it("Should be case-sensitive")
    def _():
        test.assert_equals(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

    @test.it("Should work with different element types")
    def _():
        test.assert_equals(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
        test.assert_equals(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])

if '__name__' == '__main__':
    sample_tests()