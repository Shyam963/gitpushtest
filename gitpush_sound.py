
import subprocess
import sys
import winsound
from pathlib import Path

SOUND_FILE = Path(__file__).parent / "push-success.mp3"


def main():
    
    command = ["git", "push", *sys.argv[1:]]

    result = subprocess.run(command)

    if result.returncode == 0:
        print("\nGitHub push successful! Playing your sound...")

        try:
            winsound.PlaySound(
                str(SOUND_FILE),
                winsound.SND_FILENAME
            )
        except RuntimeError as error:
            print(f"Could not play sound: {error}")
    else:
        print("\nPush failed. No sound played.")

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
