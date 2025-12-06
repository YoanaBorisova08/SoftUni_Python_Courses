from project.artifacts.base_artifact import BaseArtifact


class ContemporaryArtifact(BaseArtifact):
    @property
    def __str__(self):
        return "Contemporary Artifact"