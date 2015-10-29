def mine_assoc_rules(isets, min_support=2, min_confidence=0.5):
    rules = []
    for key in sorted(isets, key=len, reverse=True):
        support = isets[key]
        if support < min_support or len(key) < 2:
            continue

        for item in key:
            left = key.difference([item])
            right = frozenset([item])
            _mine_assoc_rules(
                left, right, item, support, isets,
                min_support, min_confidence, rules)

    return rules


def _mine_assoc_rules(
        left, right, last_item, rule_support, isets, min_support,
        min_confidence, rules):
    if not left:
        return

    support_a = isets[left]
    confidence = float(rule_support) / float(support_a)
    if confidence >= min_confidence:
        rules.append((left, right, rule_support, confidence))
        # We can try to increase right!
        for item in left:
            if item > last_item: continue
            new_left = left.difference([item])
            new_right = right.union([item])
            _mine_assoc_rules(
                new_left, new_right, item, rule_support, isets,
                min_support, min_confidence, rules)

