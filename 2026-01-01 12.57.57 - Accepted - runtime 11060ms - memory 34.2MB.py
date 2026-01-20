class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        
        # Build a Trie for all prefixes
        class TrieNode:
            def __init__(self):
                self.children = {}
        
        root = TrieNode()
        
        # Insert all words into trie
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
        
        # dp[i] = minimum strings to form target[0:i]
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            
            # Try to extend from position i using prefixes
            node = root
            j = i
            while j < n and target[j] in node.children:
                node = node.children[target[j]]
                j += 1
                # We can use prefix of length (j-i) to cover target[i:j]
                dp[j] = min(dp[j], dp[i] + 1)
        
        return dp[n] if dp[n] != INF else -1