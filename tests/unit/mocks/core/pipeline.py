from chilo_api.core.interfaces.pipeline import PipelineInterface


class DummyPipeline(PipelineInterface):
    @property
    def steps(self):
        return []

    @property
    def stream_steps(self):
        return []
