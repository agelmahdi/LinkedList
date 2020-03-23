class Node(object):

    def __init__(self,data):
        self.data = data;
        self.nextNode = None;

        def remove(self, data, perviousNode):
            if data == data:
                perviousNode.nextNode = self.nextNode;
                del self.data;
                del self.nextNode;
            else:
                if self.nextNode is not Node:
                    self.nextNode.remove(data, self)