class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr)
            return nullptr;

        Node* leftmost = root;

        while (leftmost->left != nullptr) {
            Node* curr = leftmost;

            while (curr != nullptr) {
                // Connect nodes inside the same parent
                curr->left->next = curr->right;

                // Connect across two different parents
                if (curr->next != nullptr) {
                    curr->right->next = curr->next->left;
                }

                curr = curr->next;
            }

            // Move to the next level
            leftmost = leftmost->left;
        }

        return root;
    }
};