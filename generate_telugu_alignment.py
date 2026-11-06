from pathlib import Path
import soundfile as sf
import tgt

src = Path("raw_data/Telugu/telugu")
dst = Path("preprocessed_data/Telugu/TextGrid/telugu")
dst.mkdir(parents=True, exist_ok=True)

count = 0

for wav in sorted(src.glob("*.wav")):
    lab = wav.with_suffix(".lab")
    if not lab.exists():
        continue

    text = lab.read_text(encoding="utf-8").strip()
    tokens = [c for c in text if not c.isspace()]

    if not tokens:
        continue

    info = sf.info(str(wav))
    duration = info.duration

    grid = tgt.TextGrid()
    tier = tgt.IntervalTier(name="phones")

    step = duration / len(tokens)

    for i, token in enumerate(tokens):
        start = i * step
        end = duration if i == len(tokens)-1 else (i+1)*step
        tier.add_interval(tgt.Interval(start, end, token))

    grid.add_tier(tier)
    tgt.io.write_to_file(grid, str(dst / (wav.stem + ".TextGrid")))

    count += 1

print("Approximate Telugu TextGrids created:", count)
