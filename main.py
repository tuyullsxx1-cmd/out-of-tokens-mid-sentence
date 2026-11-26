from pathlib import Path

LINE = "Error: out of tokens mid-sentence. The brilliant conclusion was right here a second ago. It has left the building."

# One line only: no newline inside, exactly one trailing newline in the file.
assert "\n" not in LINE
# Cap from the bounty brief: the line must fit in 140 characters.
assert len(LINE) <= 140
# The joke needs the cut-off mid-thought: the sentence must stop, not trail off.
assert LINE.endswith("building.")

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(LINE + "\n", encoding="utf-8")
