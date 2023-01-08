import unittest

from pydo.models.BasicNode import BasicNode
from pydo.models.DirectedAcyclicGraph import DirectedAcyclicGraph


class TestDependencyResolver(unittest.TestCase):
    def test_basic_traversal(self):
        target = BasicNode("Dependency")
        dependency = BasicNode("Target")
        target.targets.add(dependency)

        sorted = list(DirectedAcyclicGraph.resolveBranch(target))
        self.assertEqual([dependency, target], sorted)

    def test_complex_traversal(self):
        node_a = BasicNode("A")
        node_b = BasicNode("B")
        node_c = BasicNode("C")
        node_d = BasicNode("D")
        node_e = BasicNode("E")

        node_a.targets.add(node_b)
        node_a.targets.add(node_c)
        node_b.targets.add(node_d)
        node_c.targets.add(node_d)
        node_d.targets.add(node_e)

        sorted = list(DirectedAcyclicGraph.resolveBranch(node_a))
        expected_first = [node_e, node_d, node_b, node_c, node_a]
        expected_second = [node_e, node_d, node_c, node_b, node_a]
        self.assertTrue(sorted == expected_first or sorted == expected_second)

    def test_fail_on_cycle(self):
        node_a = BasicNode("A")
        node_b = BasicNode("B")
        node_a.targets.add(node_b)
        node_b.targets.add(node_a)

        with self.assertRaises(RuntimeError):
            list(DirectedAcyclicGraph.resolveBranch(node_a))


if __name__ == '__main__':
    unittest.main()
