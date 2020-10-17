from unittest import TestCase, main
from time import time


class ProblemTests(TestCase):
    def setUp(self):
        self.startTime = time()

    def tearDown(self):
        t = time() - self.startTime
        print(f'{self.id()} ran in {t:.4f}s.')

    def test_problem_1(self):
        from problem_1 import problem_1
        self.assertEqual(problem_1(), 233168)

    def test_problem_2(self):
        from problem_2 import problem_2
        self.assertEqual(problem_2(), 4613732)

    def test_problem_3(self):
        from problem_3 import problem_3
        self.assertEqual(problem_3(), 6857)

    def test_problem_4(self):
        from problem_4 import problem_4
        self.assertEqual(problem_4(), 906609)

    def test_problem_5(self):
        from problem_5 import problem_5
        self.assertEqual(problem_5(), 232792560)

    def test_problem_6(self):
        from problem_6 import problem_6
        self.assertEqual(problem_6(), 25164150)

    def test_problem_7(self):
        from problem_7 import problem_7
        self.assertEqual(problem_7(), 104743)

    def test_problem_8(self):
        from problem_8 import problem_8
        self.assertEqual(problem_8(), 23514624000)

    def test_problem_9(self):
        from problem_9 import problem_9
        self.assertEqual(problem_9(), 31875000)

    def test_problem_10(self):
        from problem_10 import problem_10
        self.assertEqual(problem_10(), 142913828922)

    def test_problem_11(self):
        from problem_11 import problem_11
        self.assertEqual(problem_11(), 70600674)

    def test_problem_12(self):
        from problem_12 import problem_12
        self.assertEqual(problem_12(), 76576500)

    def test_problem_13(self):
        from problem_13 import problem_13
        self.assertEqual(problem_13(), 5537376230)

    def test_problem_14(self):
        from problem_14 import problem_14
        self.assertEqual(problem_14(), 837799)

    def test_problem_15(self):
        from problem_15 import problem_15
        self.assertEqual(problem_15(), 137846528820)

    def test_problem_16(self):
        from problem_16 import problem_16
        self.assertEqual(problem_16(), 1366)

    def test_problem_17(self):
        from problem_17 import problem_17
        self.assertEqual(problem_17(), 21124)

    def test_problem_18(self):
        from problem_18 import problem_18
        self.assertEqual(problem_18(), 1074)

    def test_problem_19(self):
        from problem_19 import problem_19
        self.assertEqual(problem_19(), 171)

    def test_problem_20(self):
        from problem_20 import problem_20
        self.assertEqual(problem_20(), 648)

    def test_problem_21(self):
        from problem_21 import problem_21
        self.assertEqual(problem_21(), 31626)

    def test_problem_22(self):
        from problem_22 import problem_22
        self.assertEqual(problem_22(), 871198282)

    def test_problem_24(self):
        from problem_24 import problem_24
        self.assertEqual(problem_24(), 2783915460)

    def test_problem_25(self):
        from problem_25 import problem_25
        self.assertEqual(problem_25(), 4782)

    def test_problem_27(self):
        from problem_27 import problem_27
        self.assertEqual(problem_27(), -59231)

    def test_problem_28(self):
        from problem_28 import problem_28
        self.assertEqual(problem_28(), 669171001)

    def test_problem_29(self):
        from problem_29 import problem_29
        self.assertEqual(problem_29(), 9183)

    def test_problem_30(self):
        from problem_30 import problem_30
        self.assertEqual(problem_30(), 443839)

    def test_problem_33(self):
        from problem_33 import problem_33
        self.assertEqual(problem_33(), 100)

    def test_problem_35(self):
        from problem_35 import problem_35
        self.assertEqual(problem_35(), 55)

    def test_problem_36(self):
        from problem_36 import problem_36
        self.assertEqual(problem_36(), 872187)

    def test_problem_39(self):
        from problem_39 import problem_39
        self.assertEqual(problem_39(), 840)

    def test_problem_40(self):
        from problem_40 import problem_40
        self.assertEqual(problem_40(), 210)

    def test_problem_41(self):
        from problem_41 import problem_41
        self.assertEqual(problem_41(), 7652413)

    def test_problem_42(self):
        from problem_42 import problem_42
        self.assertEqual(problem_42(), 162)

    def test_problem_43(self):
        from problem_43 import problem_43
        self.assertEqual(problem_43(), 16695334890)

    def test_problem_45(self):
        from problem_45 import problem_45
        self.assertEqual(problem_45(), 1533776805)

    def test_problem_47(self):
        from problem_47 import problem_47
        self.assertEqual(problem_47(), 134043)

    def test_problem_48(self):
        from problem_48 import problem_48
        self.assertEqual(problem_48(), 9110846700)

    def test_problem_52(self):
        from problem_52 import problem_52
        self.assertEqual(problem_52(), 142857)

    def test_problem_53(self):
        from problem_53 import problem_53
        self.assertEqual(problem_53(), 4075)

    def test_problem_55(self):
        from problem_55 import problem_55
        self.assertEqual(problem_55(), 249)

    def test_problem_56(self):
        from problem_56 import problem_56
        self.assertEqual(problem_56(), 972)

    def test_problem_58(self):
        from problem_58 import problem_58
        self.assertEqual(problem_58(), 26241)

    def test_problem_67(self):
        from problem_67 import problem_67
        self.assertEqual(problem_67(), 7273)

    def test_problem_69(self):
        from problem_69 import problem_69
        self.assertEqual(problem_69(), 510510)

    def test_problem_74(self):
        from problem_74 import problem_74
        self.assertEqual(problem_74(), 402)

    def test_problem_92(self):
        from problem_92 import problem_92
        self.assertEqual(problem_92(), 8581146)

    def test_problem_97(self):
        from problem_97 import problem_97
        self.assertEqual(problem_97(), 8739992577)

    def test_problem_99(self):
        from problem_99 import problem_99
        self.assertEqual(problem_99(), 709)

    def test_problem_102(self):
        from problem_102 import problem_102
        self.assertEqual(problem_102(), 228)


if __name__ == "__main__":
    main()
