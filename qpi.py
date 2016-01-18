# [\0]
# Tamar Labs 2016.
#
# @authors: Adam Lev-Libfeld (adam@tamarlabs.com)
#

import sys
from time import time
import socket
import common.logger

from kombu import BrokerConnection, Consumer, Queue
from kombu.mixins import ConsumerMixin

CONSOLE_PRINT = False


class QPI(ConsumerMixin):

    def __init__(self, module, logger, rabbitmq_connection_str, intake_queue_name, output_queue_name,serializer='json', compression=None):
        self._logger = logger
        self.module = module
        self.connection = BrokerConnection(rabbitmq_connection_str)
        self.qin = Queue(intake_queue_name)
        self.qout = connection.SimpleQueue(output_queue_name)
        self.serializer = serializer
        self.compression = compression

    def get_consumers(self, Consumer, default_channel):
        #TODO: consider adding a QoS attribute (prefetch) to consumers for improved performance
        return [
            Consumer(queues=self.qin, callbacks=[self.on_call]),
        ]


    def on_consumer_end(self, connection, default_channel):
        pass


    def on_call(self, payload, msg_obj):
        request_id =  payload[0]
        method_name = payload[1]
        argument_list = payload[2:]
        methodToCall = getattr(self.module, method_name)
        result = methodToCall(*argument_list)
        self.qout.put({'id' : request_id,
                       'result' : result,
                       'hostname': socket.gethostname(),
                       'timestamp': time()
                       },
                       serializer=self.serializer,
                       compression=self.compression)
