#!/usr/bin/env python3
"""Offline Stephen Curry UI task graph checker.

Checks dependencies and overlapping writes, not live Codex Agent scheduling.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path, PurePosixPath


class WorkflowError(ValueError):
    pass


def _normalized(p: str):
    if not isinstance(p, str) or not p or '\\' in p or p.startswith('/') or '..' in PurePosixPath(p).parts:
        raise WorkflowError(f'Unsafe task path: {p!r}')
    return p.rstrip('/')


def _overlap(a: str, b: str) -> bool:
    return a == b or a.startswith(b + '/') or b.startswith(a + '/')


def validate_task_graph(tasks):
    if not isinstance(tasks, list):
        raise WorkflowError('Expected a list of tasks')
    ids = [t.get('task_id') for t in tasks]
    if any(not isinstance(x, str) or not x for x in ids) or len(ids) != len(set(ids)):
        raise WorkflowError('Each task must have a unique non-empty task_id')
    by_id = dict(zip(ids, tasks))
    for task in tasks:
        if task.get('access') not in {'read', 'write'}:
            raise WorkflowError('Each task must set access=read|write')
        if not isinstance(task.get('dependencies'), list) or not isinstance(task.get('allowed_paths'), list):
            raise WorkflowError('Tasks require dependencies[] and allowed_paths[]')
        for dep in task['dependencies']:
            if dep not in by_id or dep == task['task_id']:
                raise WorkflowError(f'Unknown/self dependency: {dep}')
        for p in task['allowed_paths']:
            _normalized(p)
    remaining = set(ids)
    ordered = []
    while remaining:
        ready = sorted(i for i in remaining if set(by_id[i]['dependencies']).issubset(set(ordered)))
        if not ready:
            raise WorkflowError('Dependency graph has a cycle')
        ordered.extend(ready)
        remaining.difference_update(ready)
    def ancestors(tid):
        found = set()
        todo = list(by_id[tid]['dependencies'])
        while todo:
            dep = todo.pop()
            if dep not in found:
                found.add(dep)
                todo += by_id[dep]['dependencies']
        return found
    cached = {tid: ancestors(tid) for tid in ids}
    for i, a in enumerate(tasks):
        for b in tasks[i+1:]:
            if a['access'] == b['access'] == 'read':
                continue
            if a['task_id'] in cached[b['task_id']] or b['task_id'] in cached[a['task_id']]:
                continue
            if any(_overlap(_normalized(p), _normalized(q)) for p in a['allowed_paths'] for q in b['allowed_paths']):
                raise WorkflowError(f"Concurrent write/read conflict: {a['task_id']} and {b['task_id']} overlap paths")
    return ordered


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--file', required=True)
    args = p.parse_args()
    try:
        tasks = json.loads(Path(args.file).read_text(encoding='utf8'))
        order = validate_task_graph(tasks)
    except (OSError, ValueError) as exc:
        print(f'BLOCKED: {exc}',file=sys.stderr)
        return 2
    print('PASS: task graph validated; safe topological order: ' + ', '.join(order))
    print('NOTICE: no live Agent scheduling or host access controls executed')
    return 0

if __name__ == '__main__': sys.exit(main())
