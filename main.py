from binary_expression_tree import BinaryExpressionTree


def main():
    expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    print("----- Binary Expression Tree -----")

    for expr in expressions:
        tree = BinaryExpressionTree()
        tree.build_tree(expr)

        print("Infix Expression:", tree.inorder())
        print("Postfix Expression:", tree.postorder())
        print("Evaluated Result:", tree.evaluate())
        print()


if __name__ == "__main__":
    main()