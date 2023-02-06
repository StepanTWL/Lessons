from unittest import TestCase, main
from Lesson61 import delayTransistorKeys


class Tests_DelayTransistorKeys(TestCase):

    def test_01(self):
        self.assertEqual(delayTransistorKeys(1, 0, 3000, 100), 1000)

    def test_02(self):
        self.assertEqual(delayTransistorKeys(2, 1, 3000, 100), 1000)




if __name__ == 'main':  # if ide not pycharm
    main()
