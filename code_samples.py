from qpi import QPI

class example_module(object):
    def __init__(self):
        self.value = 0

    def get(self):
        return self.value

    def set(self, new_value):
        self.value = new_value


def module_example():
    connection_str = 'librabbitmq://guest:guest@%s:%s//' % ("localhost", "5672")
    consumer = QPI(example_module, "", "intake_queue", "output_queue")
    consumer.run()

def script_example():
    import script_wrapper
    script_as_module = script_wrapper("echo")
    connection_str = 'librabbitmq://guest:guest@%s:%s//' % ("localhost", "5672")
    consumer = QPI(script_as_module, "", "intake_queue", "output_queue")
    consumer.run()
    pass
