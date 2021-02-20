class Order(object):
    m = 0
    t2 = 0
    t3  = 0
    t4 = 0
    pizzas = []

    @staticmethod
    def create(data):
        order = Order()

        m, t2, t3, t4 = data[0].split(' ')
            
        order.m = int(m)
        order.t2 = int(t2)
        order.t3 = int(t3)
        order.t4 = int(t4)

        for line in data[1:]:
            tokens = line.split(' ')
            order.pizzas.append(tokens[1:])  

        return order


    @staticmethod
    def load_from_file(filename):
        order = None
        with open(filename,'r') as fin:
            lines = fin.readlines()
            order = Order.create(data)
        return order

            


