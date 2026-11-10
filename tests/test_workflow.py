import importlib.util
import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('workflow',R/'tools/workflow.py')
workflow=importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


def task(id,deps,paths,access='write'):
    return dict(task_id=id,dependencies=deps,allowed_paths=paths,access=access)

class GraphTest(unittest.TestCase):
    def test_independent_reads_and_sequenced_writes(self):
        tasks=[task('research',[],['docs/'],'read'),task('design',['research'],['src/']),task('qa',['design'],['src/'],'read')]
        self.assertEqual(workflow.validate_task_graph(tasks),['research','design','qa'])

    def test_cyclic_dependency(self):
        with self.assertRaisesRegex(workflow.WorkflowError,'cycle'):
            workflow.validate_task_graph([task('a',['b'],['src/a']),task('b',['a'],['src/b'])])

    def test_parallel_overlap_blocked(self):
        with self.assertRaisesRegex(workflow.WorkflowError,'conflict'):
            workflow.validate_task_graph([task('a',[],['src']),task('b',[],['src/Hero.tsx'])])

    def test_read_only_independent_is_ok(self):
        tasks=[task('art',[],['src/'],'read'),task('ux',[],['src/'],'read')]
        self.assertEqual(len(workflow.validate_task_graph(tasks)),2)

    def test_unknown_dep_and_traversal(self):
        with self.assertRaises(workflow.WorkflowError):
            workflow.validate_task_graph([task('x',['missing'],['src/a'])])
        with self.assertRaises(workflow.WorkflowError):
            workflow.validate_task_graph([task('x',[],['../etc/passwd'])])

if __name__=='__main__': unittest.main()
