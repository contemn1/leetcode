from collections import defaultdict, deque
class TrieNode(object):
    __slots__ = ['value', 'next', 'fail', 'emit']

    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.fail = None
        self.emit = None


class AhoCorasic(object):
    
    def __init__(self, words):
        self.root = self.build_trie(words)

    def build_trie(self, words):
        assert isinstance(words, list) and words
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node = node.next[c]
            if not node.emit:
                node.emit = {word}
            else:
                node.emit.add(word)
        return root

    
    def build_failure_pointers(self):
        queue = deque()
        queue.append((None, self.root, None))
        while queue:
            val, curr, parent = queue.popleft()
            for char, sub in curr.next.items():
                queue.append((char, sub, curr))
            if parent is None:
                continue
            elif parent is self.root:
                curr.fail = self.root
            else:
                fail = parent.fail
                while fail and val not in fail.next:
                    fail = fail.fail
                if fail:
                    curr.fail = fail.next[val]
                else:
                    curr.fail = self.root

    def search(self, s):
        seq_map = {}
        node = self.root
        for i, c in enumerate(s):
            matched = True
            while c not in node.next:
                if not node.fail:
                    matched = False
                    node = self.root
                    break
                node = node.fail
            if not matched:
                continue
            node = node.next[c]
            if node.emit:
                for _ in node.emit:
                    from_index = i + 1 - len(_)
                    if from_index not in seq_map:
                        seq_map[from_index] = [_]
                    else:
                        seq_map[from_index].append(_)
        return seq_map

if __name__ == "__main__":
    words = ["foo", "bar"]
    ac_automata = AhoCorasic(words)
    ac_automata.build_failure_pointers()
    s = "foobarthebarfooman"
    res = ac_automata.search(s)
    print(res)
