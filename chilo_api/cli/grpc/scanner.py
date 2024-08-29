import glob
import os


class GRPCScanner:

    def get_handler_glob_pattern(self, handlers_base):
        if '*' in handlers_base and '.py' in handlers_base:
            return handlers_base
        return handlers_base + os.sep + '**' + os.sep + '*.py'

    def get_generated_glob_pattern(self, protobuf_base):
        return protobuf_base + os.sep + '**' + os.sep + '*_pb2*.py'

    def get_gprc_handers(self, handlers_base):
        handler_pattern = self.get_handler_glob_pattern(handlers_base)
        return glob.glob(handler_pattern, recursive=True)
