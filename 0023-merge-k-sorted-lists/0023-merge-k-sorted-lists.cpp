class Solution {
public:

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* curr = &dummy;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;
            }

            curr = curr->next;
        }

        if (l1)
            curr->next = l1;
        else
            curr->next = l2;

        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
            return nullptr;

        int n = lists.size();

        while (n > 1) {
            int index = 0;

            for (int i = 0; i < n; i += 2) {
                if (i + 1 < n)
                    lists[index++] = mergeTwoLists(lists[i], lists[i + 1]);
                else
                    lists[index++] = lists[i];
            }

            n = index;
        }

        return lists[0];
    }
};