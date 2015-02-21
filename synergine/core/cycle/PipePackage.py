from synergine.lib.process.processmanager import PipePackage as BasePipePackage

class PipePackage(BasePipePackage):
    """
    Object used to send data to process
    """

    def set_context(self, context):
        self._context = context

    def get_context(self):
        return self._context

    def set_mechanisms(self, mechanisms):
        self._mechanisms = mechanisms

    def get_mechanisms(self):
        return self._mechanisms

    def setCurrentProcessId(self, process_id):
        super().setCurrentProcessId(process_id)
        self._context.set_current_chunk_position(process_id)

    def setCountProcess(self, count):
        super().setCountProcess(count)
        self._context.set_total_chunk(count)