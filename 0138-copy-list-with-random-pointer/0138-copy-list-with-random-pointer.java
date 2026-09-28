class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        HashMap<Node, Node> map = new HashMap<>();

        // Pass 1: Create a copy of every node
        Node curr = head;

        while (curr != null) {
            map.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        // Pass 2: Connect next and random pointers
        curr = head;

        while (curr != null) {
            Node clone = map.get(curr);

            clone.next = map.get(curr.next);
            clone.random = map.get(curr.random);

            curr = curr.next;
        }

        return map.get(head);
    }
}