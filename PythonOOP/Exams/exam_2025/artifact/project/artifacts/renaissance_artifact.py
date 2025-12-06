from project.artifacts.base_artifact import BaseArtifact


class RenaissanceArtifact(BaseArtifact):
    @property
    def __str__(self):
        return "Renaissance Artifact"