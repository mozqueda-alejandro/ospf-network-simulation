class Link:
    counter = 0
    link_restore_time = 3

    def __init__(self, cost, link_failure_probability):
        self.link_id = Link.counter
        self.cost = cost
        self.link_failure_probability = link_failure_probability
        self.link_status = True  # True = link is active, False = link is inactive
        Link.counter += 1

    def __str__(self):
        return f'Link cost: {self.cost} / Link failure probability: {self.link_failure_probability}'
