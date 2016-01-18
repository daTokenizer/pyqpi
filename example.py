import qpi

class example_module(object):
    def __init__(self):
        self.value = 0

    def get(self):
        return self.value

    def set(self, new_value):
        self.value = new_value


def module_example():
    pass

def script_example():
    import script_wrapper
    pass

def test():
    pass

def get_func_result(self, module, method_name, argument_list):
    methodToCall = getattr(module, method_name)
    return methodToCall(*argument_list)

def print_usage(cmd):
    #todo: all add subcommands should be under $ fever.py add <sub command> <params>
    print "usage: %s --help/-h/-?" % cmd
    print "   or: %s --module" % cmd
    print "   or: %s --script" % cmd
    print "   or: %s --test" % cmd
    #TODO: add some explaining of what's going on

if __name__ == "__main__":
    import sys
    should_print_usage = False
    prog = sys.argv[0]
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd in ("help","--help","-h","-?"):
            should_print_usage = True
        elif cmd in ("test","--test"):
            test()
        elif len(sys.argv) > 2:
            if cmd in ("add","--add"):
                item_url = sys.argv[2]
                if len(sys.argv) > 3:
                    network = sys.argv[3]
                else:
                    network = "facebook"
                print "adding %s item %s" % (network,item_url)
                print "response:"
                print safely_add_item(item_url, network=network, fetchUserId=2,targetUserId=1)

            elif cmd == "read":
                item_identifier = sys.argv[2]
                print "settine item %s as read" % item_identifier
                print "response:"
                print set_item_read(item_identifier)
        else:
            should_print_usage = True
            print "unknown command '%s'" % cmd

    if should_print_usage:
        print_usage(prog)
    else:
        sys.exit(0)
