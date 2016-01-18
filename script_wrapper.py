import subprocess

RUN_FUNCTION_NAME = "run"

class script_wrapper(object):
    def __init__(self, script_path):
        self.script = script_path

    def run(self, args):
        call_item_list = [self.script]
        for arg in args:
            try:
                string_arg = str(arg)
                call_item_list.append(string_arg)
            except:
                pass
        output = subprocess.check_output(call_item_list)
        return output
