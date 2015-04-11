#!/bin/env python2

import solution
import unittest

class Test(unittest.TestCase):

    def test_base(self):
        input_key = '6JUPiyB8BBcydqprLyoadMWuWyhBxsaRu2YPpMRMfa93tRhKQ97'
        public_key = 'DHjmUqaaYBfDpyFvD9H8RjafbFy7cU5fGa'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

    def test_1swap(self):
        input_key = '6JUPiyB8BBcydqpMLyoadMWuWyhBxsaRu2YPpMRrfa93tRhKQ97'
        public_key = 'DHjmUqaaYBfDpyFvD9H8RjafbFy7cU5fGa'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

    def test_3swaps(self):
        input_key = '6PJUiyB8BBcydqpMLyoadMWuWyhBxsaRu2YPpMRrfa93tRhKQ79'
        public_key = 'DHjmUqaaYBfDpyFvD9H8RjafbFy7cU5fGa'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

    def test_halfswap(self):
        input_key = '6hBxsaRu2YPpMRMfa93tRhKQ97JUPiyB8BBcydqprLyoadMWuWy'
        public_key = 'DHjmUqaaYBfDpyFvD9H8RjafbFy7cU5fGa'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

    def test_rotate(self):
        input_key = '6B8BBcydqprLyoadMWuWyhBxsaRu2YPpMRMfa93tRhKQ97JUPiy'
        public_key = 'DHjmUqaaYBfDpyFvD9H8RjafbFy7cU5fGa'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

    def test_dogefu(self):
        # reddit.com/r/dogecoin/comments/303sj9/dogefu_key_origami/

        #input_key = '6KUsZfnpC35S4J92BiJfY6g7oi94PDwiHDPFxUAzkQtfdut2oWw'

        # Swap first and last blocks
        #input_key = '6 t2oWw npC35 S4J92 BiJfY 6g7oi 94PDw iHDPF xUAzk Qtfdu KUsZf'

        # Swap first and second halves
        #input_key = '6 94PDw iHDPF xUAzk Qtfdu t2oWw KUsZf npC35 S4J92 BiJfY 6g7oi'

        # Reverse characters of first block
        #input_key = '6 wDP49 iHDPF xUAzk Qtfdu t2oWw KUsZf npC35 S4J92 BiJfY 6g7oi'

        input_key = '6wDP49iHDPFxUAzkQtfdut2oWwKUsZfnpC35S4J92BiJfY6g7oi'
        public_key = 'DPXVGzs1ttpo1sDQ6xaqCc8WRY1HPurn3i'
        self.assertEqual(solution.answer(input_key, public_key), public_key)


    def test_final(self):
        input_key = '6KTnTsUJ1cryy3Kyb28yWNuiWiTvvMWU1MtHYiN4oMRTeDqb9jD'
        public_key = 'DQ7Ys3fkuCHjt5dg4yHTcNB8t7FwM3AQSJ'
        self.assertEqual(solution.answer(input_key, public_key), public_key)

if __name__ == '__main__':
    unittest.main()
