class ProgressTracker:

    def __init__(self):
        self.reset()

    def reset(self):
        self.stage = "Idle"
        self.progress = 0
        self.files = 0
        self.chunks = 0
        self.current_chunk = 0
        self.total_chunks = 0

    def update(
        self,
        stage=None,
        progress=None,
        files=None,
        chunks=None,
        current_chunk=None,
        total_chunks=None,
    ):

        if stage is not None:
            self.stage = stage

        if progress is not None:
            self.progress = progress

        if files is not None:
            self.files = files

        if chunks is not None:
            self.chunks = chunks

        if current_chunk is not None:
            self.current_chunk = current_chunk

        if total_chunks is not None:
            self.total_chunks = total_chunks

    def to_dict(self):

        return {
            "stage": self.stage,
            "progress": self.progress,
            "files": self.files,
            "chunks": self.chunks,
            "current_chunk": self.current_chunk,
            "total_chunks": self.total_chunks,
        }


tracker = ProgressTracker()