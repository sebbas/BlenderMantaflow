# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

import unittest
import os
import sys

from render_layer_common import *


# ############################################################
# Testing
# ############################################################

class UnitTesting(RenderLayerTesting):
    def test_render_settings(self):
        """
        See if the depsgraph evaluation is correct
        """
        clay = Clay(extra_kid_layer=True)
        self.assertEqual(clay.get('object', 'matcap_icon'), '01')

        clay.set('kid', 'matcap_icon', '02')
        clay.set('extra', 'matcap_icon', '04')
        self.assertEqual(clay.get('object', 'matcap_icon'), '04')


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()