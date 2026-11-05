import csv
import io
import os

import soundfile as sf
from datasets import load_dataset, Audio

base = "data/English"
os.makedirs(f"{base}/wavs", exist_ok=True)

with open(f"{base}/selection_manifest.csv", newline="", encoding="utf-8") as f:
    selected = {int(row["sample_index"]): row for row in csv.DictReader(f)}

ds = load_dataset(
    "ai4bharat/Svarah",
    split="test",
    streaming=True
).cast_column("audio_filepath", Audio(decode=False))

saved = 0
failed = 0

for index, sample in enumerate(ds):
    if index not in selected:
        continue

    row = selected[index]
    filename = f"{row['split']}_{index:05d}"
    wav_path = f"{base}/wavs/{filename}.wav"

    try:
        if not os.path.exists(wav_path):
            audio_bytes = sample["audio_filepath"]["bytes"]
            if audio_bytes is None:
                raise ValueError("Audio bytes missing")

            audio, sr = sf.read(io.BytesIO(audio_bytes))
            sf.write(wav_path, audio, sr)

        with open(f"{base}/wavs/{filename}.txt", "w", encoding="utf-8") as f:
            f.write(row["text"])

        saved += 1
        if saved % 100 == 0:
            print(f"Saved {saved}/{len(selected)} recordings", flush=True)

    except Exception as e:
        failed += 1
        print(f"Failed sample {index}: {e}", flush=True)

    if saved + failed == len(selected):
        break

print("Download finished")
print("Saved:", saved)
print("Failed:", failed)
