import git
from git.exc import GitCommandError

class GitService:
    """
   clase para interactuar con un repositorio de Git.
    """
    def __init__(self, repo_path: str = '.'):
        """
        Inicializa el servicio de Git.
        :param repo_path: La ruta al repositorio. Por defecto, es el directorio actual.
        """
        try:
            self.repo = git.Repo(repo_path, search_parent_directories=True)
        except git.InvalidGitRepositoryError:
            print("Error: No es un repositorio de Git válido.")
            exit(1)

    def get_staged_diff(self) -> str | None:
        """
        obtengo los cambios que están en el "staging area" (añadidos con 'git add').

        :return: Una cadena con el diff, o None si no hay nada en el staging area.
        """
        # comparo el HEAD (el último commit) con el index (staging area)
        diff = self.repo.git.diff('--staged')

        if not diff:
            print("No hay cambios en el 'staging area'. Usa 'git add' para añadir archivos al commit.")
            return None

        return diff